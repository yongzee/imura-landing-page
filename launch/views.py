from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FeedbackForm, WaitlistForm


def landing_page(request):

    # ALWAYS define forms first (prevents UnboundLocalError)
    feedback_form = FeedbackForm()
    waitlist_form = WaitlistForm()

    if request.method == "POST":

        # FEEDBACK FORM
        if "feedback_submit" in request.POST:
            feedback_form = FeedbackForm(request.POST)

            if feedback_form.is_valid():
                feedback_form.save()
                messages.success(
                    request,
                    "✅ Feedback received successfully. We appreciate your input!"
                )
                return redirect("landing_page")

        # WAITLIST FORM
        elif "waitlist_submit" in request.POST:
            waitlist_form = WaitlistForm(request.POST)

            if waitlist_form.is_valid():
                waitlist_form.save()
                messages.success(
                    request,
                    "🚀 You're on the waitlist! We'll notify you when Imura launches."
                )
                return redirect("landing_page")

    return render(request, "landing_page.html", {
        "feedback_form": feedback_form,
        "waitlist_form": waitlist_form,
    })