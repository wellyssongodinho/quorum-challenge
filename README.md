# Coding Challenge
Working with Legislative Data
<div id="top"></div>

## :truck: Deliverables

<p align="center">
  <a href="#rocket-tecnologies">Tech</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#layout">Layout</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#construction-roadmap">Roadmap</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribure">How to contribure</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

## :rocket: Tecnologia

You will use the following tools to build your application:

* [![Python][Python.org]][Python-url]

<div id="project"></div>
## 💻 Project

The project aims to solve the challenge proposed and detailed in the documentation [Quorum Coding Challenge Legislative Data](./Quorum%20Coding%20Challenge%20Legislative%20Data.pdf).

<div id="layout"></div>
## 🔖 Layout

See [Quorum Coding Challenge Legislative Data](./Quorum%20Coding%20Challenge%20Legislative%20Data.pdf)

## :construction: Roadmap

After completing your implementation, you should include a write up that answers the following
questions:

* [x] 1. Discuss your solution’s time complexity. What tradeoffs did you make?
The solution is aimed at solving simple calculations about entities involved in the process. It is necessary to know entity relationship rules to understand the logic and calculations required.
* [x] 2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?
I would create an automatic reading for columns informing the desired type of calculation and modify the code to support this automation
* [x] 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
Reading through list or file has the same result. The code uses Dataframes that mostly compose multidimensional arrays. Simply changing the input data, the calculation and the generation of the CSV file would not need to be modified.
* [x] 4. How long did you spend working on the assignment?
A total of 3.5 hours were spent considering the entire process.

You should send us a folder that contains the following:

* [x] Source code for your implementation, including steps to run your code
* [x] Output files, as requested
**Importing**: the files name output was changed and the dataframes files was moved for folder data
* [x] A writeup that responds to the questions asked above

<div id="contribure"></div>
## 🤔 How to contribure

* Fork this repository;
* Create a branch with your feature: `git checkout -b <my feature>`;
* Make a commit: `git commit -m 'feat: <my feature>'`;
* Push your branch: `git push origin <my feature>`.

After, merging of your code, you can delete your branch.

<div id="license"></div>
## :memo: License

Does not applies the license

## For run you project

### Requirements

* [Python.js](https://python.org/)

#### Clone the repository

```bash
git clone https://github.com/wellyssongodinho/quorum-challenge.git
```

#### Running the code

```bash
# Calculete how many bills did the legislator support (voted for the bill) and how many bills did the legislator oppose.
$ python3 legislators-count-opt1.py
#or
$ python3 legislators-count-opt2.py

#Calculate how many legislators supported the bill and How many legislators opposed the bill and Who was the primary sponsor of the bill
$ python3 bills-count-opt1.py
#or
$ python3 bills-count-opt2.py
```

<p align="right">(<a href="#top">back to top</a>)</p>

<h1 id="autor">Autor</h1>

* [![Linkedin][Linkedin]][Linkedin-url]
* [![Gmail][Gmail]][Gmail-url]

[Gmail]: https://img.shields.io/badge/-wellysson.gomes@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:wellysson.gomes@gmail.com
[Gmail-url]: mailto:wellysson.gomes@gmail.com


[Linkedin]: https://img.shields.io/badge/-Wellysson_Godinho-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wellyssongodinho-236170234/
[Linkedin-url]: https://linkedin.com/in/wellyssongodinho/
[MUI.com]: https://img.shields.io/badge/MUI-007FFF?style=for-the-badge&logo=mui&logoColor=white
[MUI-url]: https://mui.com/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=#000000
[Next-url]: https://nextjs.org/

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[TypeScript.org]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org
