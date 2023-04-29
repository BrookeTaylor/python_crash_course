# Installing pytest with pip

> While Python includes a lot of functionality in the standard library, Python developers also depend heavily on third-party packages. A *third-party package* is a library that's developed outside the core Python language. Some popular third-party libraries are eventually adopted into the standard library, and end up being included in msot Python installations from that point forward. This happens most often with libraries that are unlikely to change much once they've had their initial bugs worked out. These kinds of libraries can evolve at the same pace as the overall language. 

> Many packages, however, are kept out of the standard library so they can be developed on a timeline independent of the language itself. These packages tend to be updated more frequently than they would be if they were tied to Python's development schedule. This is true of pytest and most of the libraries we'll use in the second half of this book. You shouldn't blindly trust every third-party packages, but you also shouldn't be put off by the fact that a lot of important functionality is implemented through such packages. 


## Updating pip

> Python includes a tool called pip that's used to install third-party packages. Because pip helps install packages from external resources, it's updated often to address potential security issues. So, we'll start by updating pip. Open a new terminal window and issue the following command:

**python -m pip install --upgrade pip**

> The first part of this command, **python -m pip**, tells Python to run the module pip. The second part, **install --upgrade**, tells pip to update a package that's already been installed. The last part, **pip**, specifies which third-party package should be updated. The output shows that my current version of pip, version 23.1

> You can use this command to update any third-party package installed on your system: 

**python -m pip install --upgrade package_name**

> Now that pip is up to date, we can install pytest: 

**python -m pip install --user pytest**

>> In my other studies, I've previously learned that you can use the following command to see a list of installed pip packages: 

**pip list**