from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMember, Portfolio, Contact, About, Service, Job, JobApplication
from .forms import TeamMemberForm, PortfolioForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def is_superuser(user):
    return user.is_superuser

def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser


@login_required
def home(request):
    return render(request, 'index.html',)



def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



@login_required
def logout_view(request):
    logout(request)
    return redirect('signup')



def is_admin(user):
    return user.is_superuser

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('signup')


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


@login_required
def team_view(request):
    members = TeamMember.objects.all()
    print("TOTAL MEMBERS:", members.count())
    return render(request, 'team.html', {'members': members})

@user_passes_test(is_staff_or_superuser)
def createTeamMember(request):
    form = TeamMemberForm()

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_view')

    context = {'form': form}
    return render(request, 'team_form.html', context)

@user_passes_test(is_staff_or_superuser)
def updateTeamMember(request, pk):
    member = TeamMember.objects.get(id=pk)
    form = TeamMemberForm(instance=member)

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_view')

    context = {'form': form}
    return render(request, 'team_form.html', context)

@user_passes_test(is_superuser)
def deleteTeamMember(request, pk):
    member = TeamMember.objects.get(id=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('team_view')
    context = {'object': member}
    return render(request, 'delete_team_member.html', context)

def portfolio_view(request):

    app = Portfolio.objects.filter(category='app')[:1]
    product = Portfolio.objects.filter(category='product')[:1]
    branding = Portfolio.objects.filter(category='branding')[:1]
    books = Portfolio.objects.filter(category='books')[:1]

    portfolios = list(app) + list(product) + list(branding) + list(books)

    context = {
        'portfolios': portfolios
    }

    return render(request, 'portfolio.html', context)



def portfolioCategory(request, category):

    portfolios = Portfolio.objects.filter(category=category)

    context = {
        'portfolios': portfolios,
        'category': category
    }

    return render(request, 'portfolio_category.html', context)

@superuser_required
def createPortfolio(request):
    form = PortfolioForm()

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')

    context = {'form': form}
    return render(request, 'portfolio_form.html', context)

@superuser_required
def updatePortfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    form = PortfolioForm(instance=portfolio)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio')

    context = {'form': form}
    return render(request, 'portfolio_form.html', context)

@superuser_required
def deletePortfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio')
    context = {'object': portfolio}
    return render(request, 'delete_portfolio.html', context)

@superuser_required
def portfolioDetails(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio-details.html', context)


def contact_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


def about(request):
    about = About.objects.first()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)

def service_view(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})


def service_details(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'service_details.html', {'service': service})

@superuser_required
def update_service(request, pk):

    service = get_object_or_404(Service, id=pk)

    if request.method == 'POST':

        service.title = request.POST.get('title')
        service.highlight = request.POST.get('highlight')
        service.description = request.POST.get('description')
        service.icon = request.POST.get('icon')

        service.save()

        messages.success(request, "Service updated successfully!")

        return redirect('services')

    context = {'service': service}

    return render(request, 'edit_service_form.html', context)

@superuser_required
def delete_service(request, pk):

    service = get_object_or_404(Service, id=pk)

    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('services')

    context = {'service': service}

    return render(request, 'delete_service.html', context)

def faq(request):
    return render(request, 'faq.html')



def career(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request, 'career.html', context)

@superuser_required
def create_job(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        requirements = request.POST.get('requirements')

        Job.objects.create(
            title=title,
            description=description,
            location=location,
            requirements=requirements
        )

        messages.success(request, "Job added successfully!")

        return redirect('career')

    return render(request,'job_form.html')


@superuser_required
def update_job(request, pk):

    job = get_object_or_404(Job, id=pk)

    if request.method == 'POST':

        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.location = request.POST.get('location')
        job.requirements = request.POST.get('requirements')

        job.save()

        messages.success(request, "Job updated successfully!")

        return redirect('career')

    context = {'job': job}

    return render(request, 'job_form.html', context)

@superuser_required
def delete_job(request, pk):

    job = get_object_or_404(Job, id=pk)

    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('career')

    context = {'job': job}

    return render(request, 'delete_job.html', context)


def job_application(request, id):

    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cv = request.FILES.get('cv')

        JobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            phone=phone,
            message=message,
            cv=cv
        )

        messages.success(request, "Your application is submitted successfully!")

        return redirect('career')

    context = {'job': job}

    return render(request,'jobapplication.html',context)
