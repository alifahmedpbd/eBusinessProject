from django.shortcuts import render, redirect
from .models import TeamMember, Portfolio
from .forms import TeamMemberForm, PortfolioForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm
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





# Signup

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


# Login
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


# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('signup')


# Admin Only View Example
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

@login_required
def portfolio_view(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios})

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


