# fastai-floydhub

[fast.ai course](http://course.fast.ai/) is fantastic, but it's too troublesome to setup an instance in AWS, use this project to setup on [FloydHub](https://www.floydhub.com) instead.

Please note that FloydHub free plan has only CPU hours but no GPU hours, it'll be slow but you will be able to complete lesson 1 just fine.

I've just tested this on lesson 1 because I'm just starting! I'll update each lesson as I go through them.


## Setup

Clone this repo and install:

    git clone https://github.com/bachew/fastai-floydhub.git
    cd fastai-floydhub
    ./bootstrap

Then activate the virtual environment:

    source .vn/bin/activate

Register an account in FloydHub and log in from browser, and then log in from command line:

    floyd login

You should see [CLI authentication token page](https://www.floydhub.com/settings/security), copy and paste the token into terminal and you'll be logged in.

Create a [new project](https://www.floydhub.com/projects/create), and initialize:

    floyd init <project_name>

Start Jupyter in FloydHub:

    ff floyd-jupyter  # provide --gpu to use GPU if you have GPU hours

Wait for it to complete and open in your browser.

Open `setup.ipynb` and follow the instructions.
