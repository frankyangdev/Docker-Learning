## practice using github actions to build docker image into docker hub ##


### Set up a Docker project ###

access Docker Hub from any workflows you create. To do this:

Add your Docker ID as a secret to GitHub project(my exmaple project [DockerDemowithGithubActions](https://github.com/frankyangdev/DockerDemowithGithubActions). 
Navigate to your GitHub repository and click Settings > Secrets > New secret.

Create a new secret with the name DOCKER_HUB_USERNAME and your Docker ID as value.

![image](https://user-images.githubusercontent.com/39177230/115870296-a3206100-a471-11eb-85f9-c5a9a5809d94.png)

Create a new Personal Access Token (PAT). To create a new token, go to Docker Hub Settings->Securities and then click New Access Token.

Let’s call this token dockerdemogithubactions.

![image](https://user-images.githubusercontent.com/39177230/115870951-85073080-a472-11eb-96c3-dc422e0f078e.png)

Now, add this Personal Access Token (PAT) as a second secret into the GitHub secrets UI with the name DOCKER_HUB_ACCESS_TOKEN.

![image](https://user-images.githubusercontent.com/39177230/115871229-dc0d0580-a472-11eb-818c-95e9a1f5b711.png)

### Set up the GitHub Actions workflow ###

In the previous section, we created a PAT and added it to GitHub to ensure we can access Docker Hub from any workflow. Now, let’s set up our GitHub Actions workflow to build and store our images in Hub. We can achieve this by creating two Docker actions:

* The first action enables us to log in to Docker Hub using the secrets we stored in the GitHub Repository.
* The second one is the build and push action.

In this example, let us set the push flag to true as we also want to push. We’ll then add a tag to specify to always go to the latest version. Lastly, we’ll echo the image digest to see what was pushed.

To set up the workflow:

* Go to your repository in GitHub and then click Actions > New workflow > Setup this workflow.
* Click set up a workflow yourself and add the following content:

**main.yml**

```
# This is a basic workflow to help you get started with Actions

name: CI to Docker Hub

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  #pull_request:
   # branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
    
      - name: Check Out Repo 
        uses: actions/checkout@v2

      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

      - name: Set up Docker Buildx
        id: buildx
        uses: docker/setup-buildx-action@v1

      - name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          context: ./
          file: ./Dockerfile
          push: true
          tags: ${{ secrets.DOCKER_HUB_USERNAME }}/DockerDemoGithubAciton-Frankyangdev:latest

      - name: Image digest
        run: echo ${{ steps.docker_build.outputs.digest }}
```        

Once edit finished, click Start Submit

![image](https://user-images.githubusercontent.com/39177230/115876420-dfa38b00-a478-11eb-9ccb-fcb28ae9dac3.png)

Last run update tagname and build failed due to upper case

![image](https://user-images.githubusercontent.com/39177230/115876250-a5d28480-a478-11eb-8864-47538024ae67.png)

Update tagname and start submit again

![image](https://user-images.githubusercontent.com/39177230/115875899-48d6ce80-a478-11eb-8edf-a557c838fe6a.png)

Check in Docker Hub

![image](https://user-images.githubusercontent.com/39177230/115875989-5e4bf880-a478-11eb-8dba-10ebc5a253d8.png)


Check in local Docker Desktop

![image](https://user-images.githubusercontent.com/39177230/115877674-49706480-a47a-11eb-90ef-aa648d79a43f.png)

Pull latest image to local and run in docker container

![image](https://user-images.githubusercontent.com/39177230/115878103-bdab0800-a47a-11eb-9bd5-f574e01f299a.png)


### Reference ###

[Configure GitHub Actions](https://docs.docker.com/ci-cd/github-actions/)



