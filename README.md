# Photova
*Photography portfolio with Django*

## Overview

Photova is a responsive, dynamic photography portfolio website. It features file upload and download capabilities to display and share work. A prospective photography client will be able to; customize how the work is displayed, categorizing images into different galleries, choose how many galleries they would like displayed publicly, and have separate detailed views for each gallery. The website is also able to provide downloadable versions of images to an end-user. This will give the client the ability to share their work with their respective clients, a necessary service to a photographer's business. A photo blog is also included with this portfolio platform as well as a django commenting system allowing end users to provide feedback on the photographer's work.


## Features

- Gallery
- Blog
- Email
- Comments

### Gallery
##### Tasks
- File upload and display
- Images stored to db via file upload
- Organize Images by Collection
- Update/edit views for admin users 

#### Usage
Admin users can upload images. They must have "is_staff" set on their user account. These images get stored to the database, but are not immediately displayed on the website until they have been included in a Collection. Collections are groupings of images according to the photographers preference or categorization. Admin users can create collections from the django admin, website admin interface, or from the "Gallery" page. These collections may then be selected for the "Showcase Gallery" which will make them publicly visible. The images that are to be included in the collection are selected in the "create collection" form. Additionally, any Permitted Users may be selected. These users will be able to view the collection from their "My Collections" page. This allows private collections to be shared with potential clients from the photographer using the following steps; A photographer creates a collection, but leaves the Showcase Gallery option unchecked. The photographer then chooses which user/(s) will be allowed to view the collection when they are logged in. All other users will be unable to view the private collection. Collections with the Showcase Gallery option checked are automatically added to the Gallery page, and should be considered the photographer's public portfolio.


