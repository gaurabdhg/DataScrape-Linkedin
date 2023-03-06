# DataScrape_linkedin

## Warning::: Data Scraping from Linkedin isn't legal and this code serves only as an example to how it could be attempted.
Any attempt made with this or any other code to scrape data from linkedin is at your own risk.

pulls data from profiels provided in a given file. 

tries to access the data, stores a 1 or 0 based on success or failure.

if succcessful the program moves onto the next else stores a unsuccessful in boolfile.

this data is first checked the next time the program is rerun so, stores a history and therefore continues from the last stop.

program knows where it was last closed off. and continues from there the next time.

if ther are some unsuccessful attempts in between the program skips over htem and runs as long as it can.

the unsuccessful runs are first attempted to scrape on the next run. If again not succcessful, its skipped and tried again on next run. otherwise the boolfile isupdated accordingly.

Multiple sleep cycles are inserted to create a lag. 

the lag time is determiend by 2/3 levels of randomiser nested with system's randomiers and irrational numbers.
