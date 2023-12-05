# Sample repo using RudderStack Transformation Action

## Breaking down the [rudderTransformation.yml](https://github.com/rudderlabs/rudder-transformation-action-code/tree/main/.github/workflows/rudderTransformation.yml)

```jsx
name: Publish Transformations to Rudder workspace
```

on: This keyword is used to define triggers on which you want to run the action. Here job gets triggered on push and pull request events on main branch.
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
```
