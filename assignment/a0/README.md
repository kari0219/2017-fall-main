# Assignment 0:  Hello W266!

This assignment is a quick walk-through to help you get set up logistically for the course.

## Due: September 7, 2017 @ 11:59 PM Pacific

**Reminder:** You may only use 2 late days for each deliverable in this course.  See the [syllabus](../../syllabus/) for details.

If you haven't yet, please:

- Sign up for [Piazza](https://piazza.com/berkeley/fall2017/datasciw266)

Now we'll get you all set up with the software packages and the course GitHub.

1. [Setup](https://calmail.berkeley.edu/manage/account/create_account) a @berkeley.edu account setup if you don't already have one (@ischool.berkeley.edu is insufficient!)

1. **Set up your computing environment:** We recommend using a Google Cloud Compute instance. We have $50 of credits available per student, and it should only take a few minutes to set up by following [our Cloud guide](cloud/).  
If you prefer to work on your own laptop/desktop/server (including AWS), we strongly recommend Ubuntu 16.04 with Anaconda 4.2.0 (Python 2.7) as your Python distribution. Be sure to install **TensorFlow version 1.1**, as the TensorFlow APIs tend to break between versions.  
*(Note that due to the variety of systems out there, we can only provide official support for Google Cloud instances.)*

2. **Clone the course repo** (if you didn't already in the Cloud guide) with:  
`git clone https://github.com/datasci-w266/2017-fall-main.git ~/w266`  
You may also want to do this on your laptop to have a local copy.  

3. **Edit the `username`** file in the `assignment/a0` folder and replace the contents with your *username@berkeley.edu* email address. *(This helps us link people to their GitHub accounts.)*.
Commit the change with `git commit`.

4. **Open and run `a0.ipynb`**. This notebook will check that your Python packages are up-to-date, test TensorFlow, and give a taste of some of the NLP datasets we'll be working with. You don't need to write any code here - just run the cells, save, and commit the updated notebook to git.

4. **Create your personal submission repo** at [this link](https://classroom.github.com/a/yuad3dqo). We'll use this for submitting assignments; it's private to you and the instructors.

5. **Run the submit script**: `./assignment/submit.sh -u your-github-username -a 0`, which will push to your personal repo. It will try to verify the submission, but you can should also visit the repo on GitHub and confirm that your changes show up.  It's your responsibility to make sure your submission has made it to GitHub!

## Next...

Continue on to [Assignment 1](../a1/).  (Unlike Assignment 0, Assignment 1 isn't just a setup exercise.  You'll want the full two weeks to work on it.  Don't wait until next week to get started!)
