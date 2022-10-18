from job_site.job_site_scraping import JobSite

instance=JobSite()
instance.landing_page()
instance.accept_cookies()
instance.search()
instance.get_and_save_data()