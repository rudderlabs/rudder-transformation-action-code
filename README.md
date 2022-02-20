# Sample repo using RudderStack Transformation Action

##Breaking down the [rudderTransformation.yml](https://github.com/rudderlabs/rudder-transformation-action-code/tree/main/.github/workflows/rudderTransformation.yml)

```jsx
name: Publish Transformations to Rudder workspace
```

on: This is used to define triggers on which you want to run the action.
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

### Action Inputs

- `email` (required) : RudderStack app workspace email.
- `accessToken` (required) : RudderStack app corresponding accessToken.
- `uploadTestArtifact` (optional) : boolean flag on whether to upload the individual transformation outputs after running the  transformation on the test events and it's diff from expected output for each.
	- When test-input-file is provided, actual outputs of all transformations with respective inputs from test-input-file are dumped into artifacts
	- When expected-output is provided, the above outputs are validated against the contents in expected-output and a diff is returned in artifacts if there is any.
	- Transformation outputs of the test data is written in its respective `camelCase(Name)_output` file
- `metaPath` (required) : The path to the meta file, the meta file let's the action know what transformations and libraries to test based on set of input events and the expected output, as well publish these transformations and libraries if the test passes.

      Meta file structure

     ```jsx
      // Meta file schema
      {
        "transformations" : <array of transformationSchema>,
        "libraries" : <array of librarySchema>
      }
     ```
      
     ```jsx
      // single transformationSchema
      {
        "file" (required): <path to the transformation code>,
        "name" (required): <transformation name>,
        "description" (optional): <transformation description>,
        "test-input-file" (optional) : <path to file containing an array of events to test the transformation>,
        "expected-output" (optional) : <path to file containing an array of expected output for the above input after running the transformation code>
      }
     ```

  > Note: If input events are not provided, transformation code will be tested againt default events. Copy of default events are shown in location `code/default_events.json`
      
     ```jsx
      // single librarySchema
      {
        "file" (required): <path to the library code>,
        "name" (required): <library name: this is the name by which to import it in any transformation code>,
        "description" (optional): <library description> ,
      }
     ```
      
     ```jsx
      // example meta.json
      {
        "transformations": [
          {
            "file": "./code/code.js",
            "name": "Transformation1",
            "description": "Description 1",
            "test-input-file": "./code/events.json",
            "expected-output": "./code/expected.json"
          },
          {
            "file": "./code/code_2.js",
            "name": "Transformation2",
            "description": "Description 2"
          }
        ],
        "libraries": [
          {
            "file": "./code/lib1.js",
            "name": "getFinanceData",
            "description": "Description 1"
          },
          {
            "file": "./code/lib2.js",
            "name": "getUserAddress",
            "description": "Description 2"
          }
        ]
      }
     ```

> Note: All paths to files above should be relative to the base repo path

