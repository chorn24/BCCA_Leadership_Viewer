from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass
from django.template.defaulttags import register


# Create your views here.
@dataclass
class Team:
    Name: str
    Description: str
    Team_Members: list[str]


Teams = {
    "management": Team(
        "Management",
        "Management team is in charge of keeping other students on track, Making and leading the teams for chores, and making sure we have all the cleaning supplies.",
        ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
    "community": Team(
        "Community",
        "Community team is in charge of coming up with events for the school, they contact places and work to bring the community together",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "documentation": Team(
        "Documentation",
        "Documentation Team is in charge of taking pictures and posting online to show and advertise the school",
        [
            "Conner",
            "Kaleigh",
            "Blair",
            "Mina",
            "Jay",
            "Joshua",
            "Kayleah",
        ],
    ),
    "procurement": Team(
        "Procurement",
        "Procurement is in charge of going out and buying items, they are also in charge of preparing food for lunch.",
        ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
}

...


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def show_info(request: HttpRequest, team_name: str) -> render:
    context = {"Team": Teams[team_name]}
    return render(request, "info.html", context)


# def show_management(request:HttpRequest) -> HttpResponse:
#     testing = Teams["Management"]
#     context = {
#         "Team":testing
#     }
#     return render(request,"management.html",context)


# def show_community(request:HttpRequest) -> HttpResponse:
#     context = {
#         "Team":Teams['Community']
#     }
#     return render(request,"community.html",context)


# def show_documentation(request:HttpRequest) -> HttpResponse:
#     context = {
#         "Team":Teams['Documentation']
#     }
#     return render(request,"documentation.html",context)


# def show_procurement(request:HttpRequest) -> HttpResponse:
#     context = {
#         "Team":Teams['Procurement']
#     }
#     return render(request,"procurement.html" ,context)


def show_team_names(request: HttpRequest) -> HttpResponse:
    context = {"Teams": Teams}
    return render(request, "index.html", context)
