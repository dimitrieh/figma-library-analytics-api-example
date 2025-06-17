## Adjusted example to extract data from 2021, 2022, and 2023

First add the following data .env file

- **FIGMA_ACCESS_TOKEN:** This is your unique Figma Personal Access Token. It can be generated from `Go to your personal menu from your avatar in https://www.figma.com/ -> Settings -> Security -> Personal access tokens -> Generate new token `. You will need to generate a new token to inherit the new `Library Analytics` permissions or equivalent. After executing the script, you can delete the token if you wish.
- **FILE_KEY:** The file key you wish to connect to. This is found in the Design System Figma file URL after `file/` something like `6p8e19mTHzCJfRfShcRH9K`.

Then just run the following, it will take you through the process of extracting the data from Figma and generating CSV files with the results.

`./script.sh`

Results are found in the `output*` folders.

---

See [original fork](https://github.com/figma-sa/figma-library-analytics-api-example) and [demo video](https://www.youtube.com/watch?v=ywQzqMERs5E).

test
