from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show=[{"title":"Cafe Dynamic Website",
                   "path":"images/project2.JPG"},
                   {
                    "title":"Steam Clone on Django-restfulAPIS",
                   "path":"images/project1.JPG"
                   },
                   {
                    "title":"E-commerce website",
                   "path":"images/project4.JPG"
                   },
                   {
                    "title":"Game Shop",
                   "path":"images/project3.JPG"
                   }]
    return render(request, "projects.html", {"projects_show": projects_show})

