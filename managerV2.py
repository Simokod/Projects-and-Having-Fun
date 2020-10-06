import tkinter as tk
from tkinter import messagebox
# from subprocess import call
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from scan_result import ScanResult

from scraper import scraper
from scraper import settings
from functools import partial
from text_analyzer import OffensivenessAnalysis
from text_analyzer import PotentialFakeNewsAnalysis
from text_analyzer import SubjectsAnalysis

def scan_specific_user(email, password, user_url):
    return

def scan_all_friends(email, password, user_url):
    return 

def scrape_and_analyze(email, password, mod, scrape_mod):
    scan_result = []
    if scrape_mod == 0:
        posts = scraper.main(email, password, mod, scrape_mod)
        profile_result = analyze_profile(posts)
        scan_result.append(profile_result)

    elif scrape_mod == 1:
        scan_result = []
        all_friends_posts = scraper.main(email.get(), password.get(), mod.get(), scrape_mod.get())
        for friend in all_friends_posts:
            friend_result = analyze_profile(friend.values())
            scan_result.append(friend_result)  

    return scan_result

# gets posts of profile. performs all analysis, and render results
def analyze_profile(posts):
    if isinstance(posts, str):
        print(posts)

    else:
        posts = posts.values()
        # perform all analyses
        offensiveness_result = OffensivenessAnalysis.analyze_profile_offensiveness(posts)
        potentialFakeNews_result = PotentialFakeNewsAnalysis.analyze_profile_potential_fake_news(posts)
        subjects_result = SubjectsAnalysis.analyze_profile_subjects(posts)

    return ScanResult(offensiveness_result, potentialFakeNews_result, subjects_result)