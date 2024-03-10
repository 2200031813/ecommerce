# from django.shortcuts import render, redirect
#
# from CommerceKart.app.forms import FeedbackForm
#
#
# # Create your views here.
# def feedback(request):
#     if request.method == 'POST':
#        form = FeedbackForm(request.POST)
#        if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the index page or wherever you want
#     else:
#         form = FeedbackForm()
#
#     context = {'form': form}
#     return render(request, 'feedback.html', context)
# # def feedback(request):
# #     return render(request,'feedback.htm