# Sample repo using RudderStack Transformation Action

##Breaking down the [rudderTransformation.yml](https://github.com/rudderlabs/rudder-transformation-action-code/tree/main/.github/workflows/rudderTransformation.yml)

```jsx
name: Publish Transformations to Rudder workspace
```

on: This is used to define triggers on which you want to run the action.In this case, the action is triggered on pushes and pull requests to the main branch.
```jsx
on: 
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  request:
    runs-on: ubuntu-latest
```
*TEST_ONLY*: this env is required to be set to false if you want to publish your transformations and libraries to Rudder workspace.
- If not provided, it defaults to true
- true - Ideal for when you are reviewing a Pull Request.
- false - Ideal for when merging to your main or any other production branch

```jsx
    env:
      TEST_ONLY: ${{ github.event_name != 'push' }}
    steps:
```
The TEST_ONLY environment variable is used to determine whether the transformations and libraries should be published to the Rudder workspace or not. If TEST_ONLY is set to true, the action will only validate the transformations and libraries without publishing them to the workspace. If TEST_ONLY is set to false, the action will publish the transformations and libraries to the workspace. In this case, the value of TEST_ONLY is determined by the github.event_name variable. If github.event_name is not equal to push, TEST_ONLY will be set to true.

This action checks out your repository into the container where the action runs
```jsx
      - uses: actions/checkout@v2
        with:
          ref: ${{ github.ref }}
```

This is the actual action as defined [here](https://github.com/marketplace/actions/rudder-transformation-action)
```jsx
      - name: Rudder Transformation Action
        uses: rudderlabs/rudder-transformation-action@1.0.0
        with:
          metaPath: './code/meta.json'
          email: 'siva.shanmukh@rudderstack.com'
          accessToken: ${{ secrets.ACCESS_TOKEN }}
          uploadTestArtifact: true
          pythonTransformations: true
```
Here are the different parameters that are being passed to the action:

- metaPath: This is the path to the meta.json file that contains the metadata for your transformations and libraries. This file is required for the action to work.
- email: This is the email address of the RudderStack account that you want to use to publish your transformations and libraries.
- accessToken: This is the RudderStack access token that is required to authenticate the action and publish your transformations and libraries.
- uploadTestArtifact: This determines whether or not to upload the transformation artifacts generated in test mode to RudderStack. Set this to true to upload artifacts in test mode.
- pythonTransformations: This is a boolean flag that determines whether or not to include Python transformations in the artifacts being uploaded. Set this to true if you have Python transformations in your repository.