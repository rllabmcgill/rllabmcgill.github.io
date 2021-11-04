# Reasoning and Learning Lab Website Redesign

[http://rl.cs.mcgill.ca/alpha](http://rl.cs.mcgill.ca/alpha)

_This webpage is currently work-in-progress, so expect heavy changes_

This repo contains the **alpha build** of the new website redesign. The existing website is hard to maintain as its a plain old html file. The proposed redesign should make website maintenance easy and can be done by anyone in the lab, directly from Github.

- Easy to maintain, as it uses Jekyll to generate webpages
- Easy to contribute, as you can just write markdown files
- Easy to update personal information, which can be made by just editing the `.yml` files
- Easy to deploy, as any PR merge will trigger remote build and push to our server

The website is powered by [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme, which is now increasingly used by many personal portfolios, labs and conferences.

## Updating information

Updating information of students, professors and alumni is very easy, and can be done even through the Github web interface. All data resides in `_data/` folder in various `.yml` files. For each profile, you should first upload an image in `assets/img/` folder.

### Updating a professor/affiliate faculty information

Edit the `_data/professors.yml` file, and add the following information:

```yaml
- name: Doina Precup
  image: dprecup.jpg
  website: https://cs.mcgill.ca/~dprecup
  description: Reinforcement Learning, Reasoning and planning under uncertainty
  scholar:
  level: core
```

Add the required information. `level` tag accepts either `core` or `affiliate`, which adds the professor's profile in the correct subheaders in [Team page](http://rl.cs.mcgill.ca/alpha/team/).

### Updating a student (postdoc/phd/msc/alumni)'s information

Edit the `_data/students.yml` file, and add the following information:

```yaml
- name: Koustuv Sinha
  image: ksinha.jpg
  website: https://cs.mcgill.ca/~ksinha4
  description: Natural Language Understanding, Systematicity & Logic in NLU, Dialog Systems # it could be research interests, or if alumni where you are now
  supervised_by: Joelle Pineau
  scholar:
  level: phd
```

Add the required information. `level` tag accepts `postdoc`, `phd`, `msc`, `alumni` for displaying profiles under the respective subheaders in [Team page](http://rl.cs.mcgill.ca/alpha/team/). For alumni, extra fields `grad_degree` and `grad_year` are required:

```yaml
- name: Ali Emami
  image: aliemami.webp
  website: http://www.cosc.brocku.ca/~aemami/
  description: Associate Professor, Brock University
  scholar:
  level: alumni
  grad_degree: PhD
  grad_year: 2021
```

This configuration will hopefully make long term maintenance easier!

## Deploying

The website currently resides in [http://rl.cs.mcgill.ca/alpha](http://rl.cs.mcgill.ca/alpha). The build and deploy Github actions are in `.github/workflows/jekyll.yml`, which is heavily inspired from this [nice blog post](https://christianspecht.de/2020/05/03/building-and-deploying-a-jekyll-site-via-github-actions/).

## Contact persons

For bug reports, feature requests, and feedback, please contact the following persons in the lab (or in Mila Slack):

- Koustuv Sinha
- Martin Klissarov
