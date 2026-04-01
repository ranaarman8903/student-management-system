from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm
from .models import Course, Assignment, Exam, AssignmentSubmit
from django.utils import timezone
from django.db.models import Q


def _group_name(user):
    g = getattr(user, 'group', None)
    return (g.name or '').strip().lower() if g else ''


def home_view(request):
    """ Render the homepage. """
    return render(request, 'home.html')


def contact_view(request):
    """ Handle contact form submission and render contact page. """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def about_view(request):
    """ Render the about page. """
    return render(request, 'about.html')


@login_required
def user_profile_view(request):
    """Display the logged-in user's profile."""
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def student_dashboard_view(request):
    """Student dashboard — users whose Role (group) is named like 'student'."""
    if _group_name(request.user) != 'student':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')

    student = request.user
    return render(request, 'dashboard.html', {'student': student})


@login_required
def teacher_dashboard_view(request):
    """Teacher dashboard — users whose Role (group) is named like 'teacher'."""
    if _group_name(request.user) != 'teacher':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')

    teacher = request.user
    assigned_courses = Course.objects.filter(teacher=teacher)
    teacher_assignments = Assignment.objects.filter(course__in=assigned_courses).order_by('due_date')

    pending_grading_count = AssignmentSubmit.objects.filter(
        assigment__in=teacher_assignments,
    ).filter(
        Q(marks__isnull=True) | Q(marks='')
    ).count()

    upcoming_exams = Exam.objects.filter(
        course__in=assigned_courses,
        date__gte=timezone.now().date(),
    ).order_by('date')

    context = {
        'teacher': teacher,
        'assigned_courses': assigned_courses,
        'teacher_assignments': teacher_assignments,
        'pending_grading_count': pending_grading_count,
        'upcoming_exams': upcoming_exams,
    }

    return render(request, 'teacher_dashboard.html', context)
