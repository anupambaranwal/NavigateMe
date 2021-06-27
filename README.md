<p align="center">
  <a href="#"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=Navigate-Me&fontSize=60%&fontColor=ffffff" alt="website title image"></a>
  <h2 align="center">This bot give users a new way to interact with Google Maps through text-based conversational interfaces.</h2>
</p>
<p align="center">
  <a href = "https://www.python.org/"><img src="https://img.shields.io/badge/language-Python-blue?style=for-the-badge"></a>
 </p>
 <p align="center">
<a href="https://github.com/anupam-b/NavigateMe/stargazers"><img src="https://img.shields.io/github/stars/anupam-b/NavigateMe?style=for-the-badge"></a>
<a href="https://github.com/anupam-b/NavigateMe/network/members"><img src="https://img.shields.io/github/forks/anupam-b/NavigateMe?style=for-the-badge"> </a>
<a href="https://github.com/anupam-b/NavigateMe/issues"><img src="https://img.shields.io/github/issues-raw/anupam-b/NavigateMe?style=for-the-badge"></a>
<a href="https://github.com/anupam-b/NavigateMe/pulls"><img src="https://img.shields.io/github/issues-pr-raw/anupam-b/NavigateMe?style=for-the-badge"></a>
</p>


##  Motivation
</p>The primary motivation of the developers of MapBot is to provide a playground to tech enthusiasts, both beginners and advanced to try algorithms, approaches and ideas while contributing to a real-life project.</p>


## ⭐ Getting Started
Refer to the following articles on the basics of Git and Github and can also contact the Project Mentors, in case you are stuck:

- [Watch this video to get started, if you have no clue about open source](https://youtu.be/SL5KKdmvJ1U)

- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)

- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request)

- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)

- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

## What are some pre-requisites?

- MySQL
  - Install the community version of mySQL from the [official mySQL documentation page](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).
  - Create root user credentials during installation.
  - Verify the installation, running the command  `mysql -uroot -p -hlocalhost` should open the mySQL monitor. (Enter the root password when prompted)
- StanfordCoreNLP
  - StanfordCoreNLP has a dependency on Java 8. `java -version` should complete successfully with version 1.8 or higher.
  - Windows- Download as a .zip file from [here](https://stanfordnlp.github.io/CoreNLP/download.html).  
  - Linux and MacOS- Follow the instructions to download the file from [here](https://stanfordnlp.github.io/CoreNLP/download.html).


## 💥 Contribution

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
- Take a look at the Existing [Issues](https://github.com/anupam-b/NavigateMe/issues) or create your own Issues!
- Wait for the Issue to be assigned to you after which you can start working on it.
- Fork the Repo and create a Branch for any Issue that you are working upon.
- Read the [Code of Conduct](https://github.com/anupam-b/NavigateMe/blob/main/CODE_OF_CONDUCT.md)
- Create a Pull Request which will be promptly reviewed and suggestions would be added to improve it.
- Add Screenshots to help us know what this Script is all about.
- Take a look at Contribution guide for Detail : [Contribution Guide](https://github.com/anupam-b/NavigateMe/blob/main/CONTRIBUTION.md)
## ⭐ Set-up and Contribution:
**1.** Fork [this](https://github.com/anupam-b/NavigateMe) repository.
Click on the <a href="https://github.com/anupam-b/NavigateMe/"><img src="https://img.icons8.com/ios/24/000000/code-fork.png"></a> symbol at the top right corner.
**2.** Clone the forked repository.
```bash
git clone https://github.com/<your-github-username>/NavigateMe
```
**3.** Create the mapbot database in mySQL
```
mysql -uroot -p -hlocalhost
```
Enter root password when prompted create database mapbot
Verify creation of the database 
```
show databases
```
**4.** Unzip the StanfordCoreNLP package in the repository and keep the file paths stanford-corenlp-x.x.x.jar and stanford-corenlp-x.x.x-models.jar handy. 

Run 
```
git update-index --assume-unchanged ENV/.env
```
Fill the existing template in ENV/.env with the corresponding values following the KEY=VALUE format

**5.**  Run 
```
python app.py
```

**6.** Navigate to the project directory.
```bash
cd NavigateMe
```

**7.** Make changes in source code.

**8.** Stage your changes and commit
```bash
#Add changes to Index
git add .
#Commit to the local repo
git commit -m "<your_commit_message>"
```

**9.** Push your local commits to the remote repo.
```bash
git push
```

**10.** Create a [PR](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) !

**11.** **Congratulations!** Sit and relax, you've made your contribution to [NavigateMe](https://github.com/anupam-b/NavigateMe/) project.

## 📢  Open Source Program

### This Project is a part of the Lets Grow More Summer of Code
<p align="center">
<img src="https://user-images.githubusercontent.com/60106112/121303829-28c07900-c919-11eb-8cf2-afd39b5c54ab.png" alt="Lets Grow More Summer of Code">
</p>

## ⭐ Issues:
For major changes, you are welcomed to open an issue and discuss what you would like to contribute. Enhancements will be appreciated.

## Hall of Fame
✨ Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
## ❤️ Project Admin
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/anupam-b">
            <img src="https://avatars.githubusercontent.com/u/66070470?s=400&u=790ee821274e85b1e152f2a0c348df46b2977a9e&v=4" width="200px;" alt="" style="border-radius:50%"/>                 <br />
            <b>anupam-b</b>
            </a><br />
            <a title="Coding">💻</a>
        </td>
    </tr>
 </table>
