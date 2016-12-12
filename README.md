# A mentor's life in an OO way

Please find all the instructions about this project in the relevant Canvas documentation.

#The story

In the near future... the seeds of Codecool have spread and many schools are opened in different parts of the world. There's no problem with the number of applicants, but (since there is a huge need for good IT professionals) it's not an easy job to attract programmers to become mentors at our schools. The main problem, is that it's really hard to describe what mentoring is about at Codecool for the possible candidates in a quick, understandable way.

Codecool's Head of HR, Humen Rajtnau (a superannuated exprogrammer from India) has a new idea: all programmers have a path to their heart, and it's called code... He thinks, that a story written in Python, instrumenting classes identified around a mentor's daily life would be perfect to get some attention in the programmers in demand.

Humen Rajtnau was a programmer long-long time ago, when the Waterfall model was used for every piece of projects around him. The project management world has evolved a lot since then, but Humen still believes that the Waterfall model is the one and only way for software development.

The thing is, that he'd like to demonstrate your work on Friday, when the annual LetsFindSomeDev conference is being held, so the deadline is strict!

#Your job

Since your mentors' payroll is deeply connected with the happiness of Humen, they would like you to satisfy his needs, and implement an Object-Oriented software on time for him, while using the Waterfall model.
#1) Requirement analysis

Your first job is to read, and understand Humen's requirements (see on the next page). He'll be around throughout this week, and you'll have a chance to ask questions from him, to clarify the project's scope. The most important thing here, is that you have to have a common understanding with Humen's about the project and his ideas.
#2) Software architecture design

Your second job is to design the software, based on Humen's requirements, his answers on your clarification questions, and your own creative ideas.
The software's design should be created in the git repository (given in the assignment), in a folder called specifications. This folder should contain a markdown file for each class (filename should equal to the class' filename, example: mentor.md) written in markdown format. 
The specification of a class should contain the following:

    the class' parent class (if any)
    the class' description
    attributes
        name
        type
        description
    class methods
        name
        list of arguments and their type
        return value
        description
    instance methods 
        name
        list of arguments
        return value
        description

Please find Humen's example specification file about one of his classes in demand in the specifications folder (codecool_class.md)

The specification folder should also contain a file for the story (story.md): a well described script what you'd like to show about a mentor's life.
#3) Implementation

When the architecture design is ready, and is approved by Humen, you can start the implementation. Please be aware, that if it turns out that the implementation cannot be done in the way the specification describes, you have to report the change need to Humen first, and if he approved it, you have to modify the specification. You can only modify the codebase afterwards. Humen is checking your repositories constantly, and he'll run riot, if he's not notified about the change in the architecture (in the specification) before the actual implementation. And if Humen runs riot, your mentors can say goodbye to their bonuses. And you don't want that, right? :-)
#4) Verification

Before the demo, you'll have some time to test your code, and fix the bugs it contains. In the verification phase, you are not allowed to put new functionalities anymore, but you can only test & fix bugs.
#5) Deployment

The deployment of your projects are actually done with keeping a demo @ Codecool for the other teams. Clapping at the end of the demo initiates the deployment process, so you don't have to press the big red button by yourself.

#Overview

I often get up sweaty recently, in the middle of the night, because of the nightmares caused by our resourcing problems... But some days ago I also had a wonderful dream, giving me a possible idea for recruiting mentors in no time.

So please find the details of my dream below:

I dreamt about projects, created by Codecoolers which advertised both their capabilities in the Object-Oriented world of Python, and the desirable life of any mentor, working in Codecool. The application basically contains many classes which can be found around a mentor. Objects are instantiated from these classes, instrumenting each other in a real-life way, demonstrating what a mentor does daily at Codecool.

You can't really imagine what a possible outcome is? My dream is foggy, but I'd like to see similar stories as the following:

 

So your job is to create similar projects (in a more funny/real-life way), which can be demonstrated on conferences/meetups and such. Methods should not only set properties on the objects, but also should print out what they did/what have happened for demo purposes.

I think this project can be implemented properly only using the Waterfall model, so please do that accordingly. 

#Mandatory classes

Although I'm counting with you to bring ideas to this project, but there are some classes which are mandatory to implement. 

#Person

We could have called this class human as well, but I don't like jokes about my name! This class represents a Person in real life, but we only use it to inherit it's features in Student and Mentor classes. Attributes: first_name: string, last_name: string, year_of_birth: integer, gender: string (male/female/notsure). The class should certainly have a constructor, which gets all the attributes above. It should raise an error, if any of the attributes is empty, and also if the provide gender is not valid

#Mentor

This class represents a mentor in real life. It should inherit all properties from the Person class, but also has some other functionalities. Attributes: nickname: string (stores the mentor's secret nickname between the students).

The class should have a method called create_by_csv, which gets a csv file path as an argument (the csv contains all the data needed to instantiate a mentor object) and gives back a list of mentors. The class should have a constructor, which calls the Person's constructor, but also set's the nickname attribute (should raise an error, if empty).

#Student

This class represents a student in real life. It should inherit all properties from the Person class, but also has some other functionalities. Attributes: knowledge_level: integer (stores the knowledge level of the student in programming), energy_level: integer (current energy level)

The class should have a method called create_by_csv, which gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object) and gives back a list of students. The class should have a constructor, which calls the Person's constructor, but also set's the attributes above (should raise an error, if any is empty).

#CodecoolClass

This class represents a class in real life. A class contains mentors and students. Attributes: location: string, year: integer, mentors: list (containing mentor objects), students: list (containing student objects)

The class should have a method called generate_local, which gets no argument and gives back a CodecoolClass object stroring some localized data in it's attributes. A CodecoolClass object can give back a mentor/student by it's full_name (given as an argument) with the find_mentor_by_full_name and find_student_by_full_name methods.

You can find this class' example specification in the repository.

#4 other mandatory classes

You have to identify at least 4 other classes, which can affect a mentor's day. Objects should be instantiated from these classes in your script. I'm really counting on you coming up wiht interesting/funny ideas, so be as creative as you can! :-)