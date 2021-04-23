
### Set up a Docker project ###

access Docker Hub from any workflows you create. To do this:

Add your Docker ID as a secret to GitHub. Navigate to your GitHub repository and click Settings > Secrets > New secret.

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

* Go to your repository in GitHub and then click Actions > New workflow.
* Click set up a workflow yourself and add the following content:

First, we will name this workflow:

