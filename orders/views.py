from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime as dt ,timedelta,time
import datetime
