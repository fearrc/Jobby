from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})

def blog(request):
	return render(request,'blog.html',{})

def blog_single(request):
	return render(request,'blog_single.html',{})

def browsejobs(request):
	return render(request,'browsejobs.html',{})

def candidates(request):
	return render(request,'candidates.html',{})

def contact(request):
	return render(request,'contact.html',{})

def job_post(request):
	return render(request,'job_post.html',{})

def new_post(request):
	return render(request,'new_post.html',{})