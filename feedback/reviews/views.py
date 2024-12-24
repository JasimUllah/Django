from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

# ------------------------------------------------------------------------------- #

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")


# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })

# ------------------------------------------------------------------------------- #

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")


# We can use to get the template of thank you page using TemplateView
# Here we don't need to add GET method instead we set a template_name adnd django will
# automatically return it for GET request

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


# Now if we want to render dynamic data in the views file we could do that with above
# template but instead we use a methon of get_context_data


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works!"
        return context


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")


# ------------------------------------------------------------------------------- #

class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context