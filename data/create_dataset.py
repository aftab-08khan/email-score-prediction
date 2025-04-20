import pandas as pd

data = {
    "email_description": [
        "Dear HR Team, I am excited to apply for the Frontend Developer position at your esteemed organization. With 3+ years of experience in React and Tailwind CSS, I believe I can contribute effectively to your development team. I have attached my resume and portfolio link for your review.",
        "Respected Hiring Manager, I recently came across the opening for the Business Analyst role. I have a strong background in analytics and dashboard tools, and would love the opportunity to bring my skills to your company.",
        "Hi there, I want to work in your company. Give me a job please. I can do many things.",
        "Get ready to WIN BIG! Click this link and grab your FREE MacBook now!",
        "Dear Recruiter, I’m writing to express my interest in the Software Engineer position. I have over 5 years of experience in Python, Django, and cloud-based solutions. I've also led teams in agile environments. Looking forward to your response.",
        "URGENT: Your PayPal account has been suspended. Click below to reactivate it.",
        "Hello HR, I am a passionate Data Scientist with expertise in machine learning and deep learning frameworks. I have completed multiple real-time projects and would like to apply for any relevant roles at your company.",
        "Hey, here’s my resume. Check it out. I need work.",
        "You’ve won a $1000 Amazon gift card! Hurry before it expires. Link inside.",
        "Dear Sir/Madam, With an MBA in Marketing and hands-on experience with digital campaigns, I am excited to submit my application for your open Marketing Lead role.",
        "Hi HR, I'm reaching out to apply for the UI/UX Designer position. I've attached my CV and some of my design samples in the portfolio link.",
        "Alert: Your system is infected. Install the attached antivirus now!",
        "Dear Hiring Team, I’m an experienced DevOps Engineer with AWS, Docker, and CI/CD experience. I admire your company’s engineering culture and am interested in contributing to your infrastructure team.",
        "Yo HR! I can code. Hire me lol.",
        "Hello, Please find attached my resume for your open position in software QA testing. I’ve worked extensively on automation frameworks and have ISTQB certification.",
        "Dear Manager, I am writing to express my sincere interest in the Remote Product Manager opportunity listed on your careers page. My resume and portfolio are linked below.",
        "This is your last chance to claim the reward. Click fast!",
        "Hello Team, as a Full Stack Developer with experience in Node.js and Next.js, I have developed scalable apps for startups. Please consider my application.",
        "Hey recruiter, I heard you’re hiring. Hit me up if you need someone.",
        "Greetings, I have a Master's in Computer Science and 4+ years of experience. I specialize in backend development using Java and Spring Boot. I would love to bring my skills to your organization."
    ],
    "contains_link": [
        True, False, False, True, False,
        True, False, False, True, False,
        True, True, False, False, False,
        True, True, False, False, False
    ],
    "contains_offer": [
        False, False, False, True, False,
        False, False, False, True, False,
        False, True, False, False, False,
        False, True, False, False, False
    ],
    "length": [len(email) for email in [
        "Dear HR Team, I am excited to apply for the Frontend Developer position at your esteemed organization. With 3+ years of experience in React and Tailwind CSS, I believe I can contribute effectively to your development team. I have attached my resume and portfolio link for your review.",
        "Respected Hiring Manager, I recently came across the opening for the Business Analyst role. I have a strong background in analytics and dashboard tools, and would love the opportunity to bring my skills to your company.",
        "Hi there, I want to work in your company. Give me a job please. I can do many things.",
        "Get ready to WIN BIG! Click this link and grab your FREE MacBook now!",
        "Dear Recruiter, I’m writing to express my interest in the Software Engineer position. I have over 5 years of experience in Python, Django, and cloud-based solutions. I've also led teams in agile environments. Looking forward to your response.",
        "URGENT: Your PayPal account has been suspended. Click below to reactivate it.",
        "Hello HR, I am a passionate Data Scientist with expertise in machine learning and deep learning frameworks. I have completed multiple real-time projects and would like to apply for any relevant roles at your company.",
        "Hey, here’s my resume. Check it out. I need work.",
        "You’ve won a $1000 Amazon gift card! Hurry before it expires. Link inside.",
        "Dear Sir/Madam, With an MBA in Marketing and hands-on experience with digital campaigns, I am excited to submit my application for your open Marketing Lead role.",
        "Hi HR, I'm reaching out to apply for the UI/UX Designer position. I've attached my CV and some of my design samples in the portfolio link.",
        "Alert: Your system is infected. Install the attached antivirus now!",
        "Dear Hiring Team, I’m an experienced DevOps Engineer with AWS, Docker, and CI/CD experience. I admire your company’s engineering culture and am interested in contributing to your infrastructure team.",
        "Yo HR! I can code. Hire me lol.",
        "Hello, Please find attached my resume for your open position in software QA testing. I’ve worked extensively on automation frameworks and have ISTQB certification.",
        "Dear Manager, I am writing to express my sincere interest in the Remote Product Manager opportunity listed on your careers page. My resume and portfolio are linked below.",
        "This is your last chance to claim the reward. Click fast!",
        "Hello Team, as a Full Stack Developer with experience in Node.js and Next.js, I have developed scalable apps for startups. Please consider my application.",
        "Hey recruiter, I heard you’re hiring. Hit me up if you need someone.",
        "Greetings, I have a Master's in Computer Science and 4+ years of experience. I specialize in backend development using Java and Spring Boot. I would love to bring my skills to your organization."
    ]],
    "is_valid": [
        1, 1, 0, 0, 1,
        0, 1, 0, 0, 1,
        1, 0, 1, 0, 1,
        1, 0, 1, 0, 1
    ]
}

df = pd.DataFrame(data)

df.to_csv("enhanced_hr_email_validation_dataset.csv", index=False)

print("Enhanced HR email validation dataset created successfully!")
