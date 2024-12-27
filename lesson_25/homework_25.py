# https://qauto2.forstudy.space/

css = """
1. div.header_left.d-flex.align-items-center a.btn.header-link[href="/"]
2. div.header_left.d-flex.align-items-center button[appscrollto="aboutSection"].btn.header-link
3. div.header_left.d-flex.align-items-center button[appscrollto="contactsSection"].btn.header-link
4. div.header_inner div.header_right.d-flex.align-items-center button.header-link.-guest
5. div.app-wrapper div.header_right button.btn.btn-outline-white
6. div.app-content div.container div.hero-descriptor h1.hero-descriptor_title.display-2
7. div.app-content div.container div.hero-descriptor button.hero-descriptor_btn.btn.btn-primary
8. div.app-content div.hero-descriptor p.hero-descriptor_descr.lead
9. div.section.about div.row div[class="col-12 col-lg-6"] div.about-block p.about-block_title.h2
10. div.section.about div.row div[class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"] div.about-block p.about-block_title.h2
11. div[class="col-12 col-lg-6"] p.about-block_descr.lead
12. div[class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"] p.about-block_title.h2
13. div[class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"] p.about-block_descr.lead
14. div.section.contacts div.container h2[_ngcontent-udb-c64]
15. div.container a.contacts_link.display-4[href="https://ithillel.ua"]
16. div.container a.contacts_link.h4[href="mailto:developer@ithillel.ua"]
17. div.contacts_socials.socials span.socials_icon.icon.icon-facebook
18. div.section.contacts div.contacts_socials.socials span.socials_icon.icon.icon-telegram
19. div.section.contacts div.contacts_socials.socials span.socials_icon.icon.icon-youtube
20. div.section.contacts div.contacts_socials.socials span.socials_icon.icon.icon-instagram
21. div.section.contacts div.contacts_socials.socials span.socials_icon.icon.icon-linkedin
22. div.footer_item.-left p:nth-of-type(1)
23. div.footer_item.-left p:nth-of-type(2)
24. div.col.footer_item.-right svg[_ngcontent-udb-c57]
25. div.ytp-cued-thumbnail-overlay div.ytp-cued-thumbnail-overlay-image
"""

xpath = """
1. //div[@class="global-layout"]// a[@class="header_logo"]
2. //div[@class="col footer_item -right"]/a[@class="footer_logo"]
3. //div[@class="header_left d-flex align-items-center"]//a[text()="Home"]
4. //div[@class="header_left d-flex align-items-center"]//button[@class="btn header-link" and contains(text(), "About")]
5. //div[@class="header_left d-flex align-items-center"]//button[@class="btn header-link" and contains(text(), "Contacts")]
6. //div[@class="header_right d-flex align-items-center"]//button[@class="header-link -guest" and contains(text(), "Guest log in")]
7. //div[@class="header_right d-flex align-items-center"]//button[@class="btn btn-outline-white header_signin" and contains(text(), "Sign In")]
8. //div[@class="hero-descriptor"]//h1[@class="hero-descriptor_title display-2" and contains(text(), "Do more!")]
9. //div[@class="hero-descriptor"]//p[@class="hero-descriptor_descr lead" and starts-with(text(), "With the help")]
10. //div[@class="col-12 col-lg-4"]//button[@class="hero-descriptor_btn btn btn-primary" and contains(text(), "Sign up")]
11. //div[@class="ytp-cued-thumbnail-overlay"]//div[@class="ytp-cued-thumbnail-overlay-image"]
12. //div[@class="container"]//p[starts-with(text(), "Hillel auto developed")]
13. //div[@class="about-block"]//p[@class="about-block_title h2" and contains(text(),"Log fuel expenses")]
14. //div[@class="col-12 col-lg-6"]//p[@class="about-block_descr lead" and starts-with(text(), "Keep")]
15. //div[@class="about-block"]//p[@class="about-block_title h2" and starts-with(text(), "Instructions")]
16. //div[@class="about-block"]//p[@class="about-block_descr lead" and starts-with(text(), "Watch")]
17. //div[@class="col-md-6 d-flex flex-column align-items-center align-items-md-start"]/h2[contains(text(), "Contacts")]
18. //div[@class="contacts_socials socials"]//span[@class="socials_icon icon icon-facebook"]
19. //div[@class="contacts_socials socials"]//span[@class="socials_icon icon icon-telegram"]
20. //div[@class="contacts_socials socials"]//span[@class="socials_icon icon icon-youtube"]
21. //div[@class="contacts_socials socials"]//span[@class="socials_icon icon icon-instagram"]
22. //div[@class="contacts_socials socials"]//span[@class="socials_icon icon icon-linkedin"]
23. //div[contains(@class, "col-md-6")]//a[@class="contacts_link display-4" and contains(text(), "ithillel.ua")]
24. //div[contains(@class, "col-md-6")]//a[@class="contacts_link h4" and contains(text(), "support@ithillel.ua")]
25. //footer[@class="footer d-flex align-items-center"]//p[contains(text(), "© 2021 Hillel IT school")]
"""
