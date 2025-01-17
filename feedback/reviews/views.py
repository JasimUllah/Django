from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# ------------------------------------------------------------------------------- #

# Create your views here.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")


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


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


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

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
# ------------------------------------------------------------------------------- #

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

# ------------------------------------------------------------------------------- #

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)