# fsf_2019_screening_task1

django-task-manager is pluggable, multi-user, mulyi-team task management
and assignment application for Django, designed to be used into an existing site as a reusable app.
django-task-manager can be user as personal to-do tracker or team task managment system.
django-task-manager is developed as screening task for felloship from fossee for year 2019.

## Features

* Search
* Comments on tasks
* Mobile-friendly
* Separate view for My Tasks and completed tasks

## Requirements

* Django 2.0+
* Python 3.6+

# Installation

django-task-manager is a Django app, not a project site. It needs a site to live in.

Put fsf_2019_screening_task1/task_manager somewhere on your Python path, or install via pip:

    pip install django-task-manager

Add to your settings:

    INSTALLED_APPS = (
        ...
        'task-manager',
    )

Create database tables:

  python manage.py migrate task_manager

Add to your URL conf:

	path('task-manger/', include('task_manager.urls')),

django-task-manager makes use of the Django `messages` system. Make sure you have installed `messages`.

## Running Tests

  python manage.py test task_manager

## Overview

1. Team can be created by any authenticated user. User that creates team is the leader of team.
   Leader has permissions to add members to team using their username.
   Lerder can revove team members using the remove button.
   Leader can delete team only if team has no members except leader.
   Only leader is allowed to assign tasks to his team.

2. Any authenticated user can create tasks. Task can be assigned to team he is leading.
   After assigning task to a team, creator can edit the task to assign task to members of team.
   Newly created task is marked as Planned. After a assigned user accepts the task, it is marked as In-Progress.
   Task can be marked as Completed by any assigned user or creator.
   Task can only be edited by creator if task is Planned(if task is In-Progress, assigned users has alreary started working on it, if there are any update comments can be used).

3. Assigned users and team members can comment on task.

4. Task assigned to team wich are not completed are shown on task detail page.
   Tasks whose due date is passed are shown with red background.

5. Tasks assigned to user wich are not completed are shown on my-tasks page.
   Tasks whose due date is passed are shown with red background.

6. Completed tasks can be seen on completed-tasks page.

7. User can search tasks by keyword.
   Tasks wich contain that keyword in title or description are shown to user(Only tasks user is allowed to see are shown)

8. User from another team is not allowed to see or comment on task
