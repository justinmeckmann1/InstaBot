# InstaBot

InstaBot is a Python-based automation tool that publishes images to Instagram using the **official Facebook / Instagram Graph API**.

Images are temporarily hosted using **imgbb** so Instagram can access them via a public URL.  
After posting, images can optionally be moved to an archive directory.

---

## Configuration

All configuration is done via a single JSON file.

### `config.json`

```json
{
    "authentication": {
        "APP_ID": "",
        "APP_SECRET": "",
        "IG_USER_ID": "",
        "SHORT_LIVED_TOKEN": "",
        "LONG_LIVED_TOKEN": "",
        "URL": "https://graph.facebook.com/v24.0/oauth/access_token",
        "IMGBB_API_KEY": ""
    },
    "data": {
        "image_dir": "./post",
        "used_image_dir": "./posted"
    },
    "settings": {
        "deleteUsedPictures": false,
        "moveUsedPictures": true
    }
}
```
## Authentication

The following fields are required to authenticate with the Facebook / Instagram Graph API.

### Required fields

#### `APP_ID`
Facebook App ID  
Location: Facebook Developer Portal → Your App → Settings → Basic

#### `APP_SECRET`
Facebook App Secret  
Location: Facebook Developer Portal → Your App → Settings → Basic

#### `IG_USER_ID`
Instagram Business or Creator account ID.  
The Instagram account **must be connected to a Facebook Page**.

#### `SHORT_LIVED_TOKEN`
Short-lived **User Access Token** generated via the Graph API Explorer.

This token must be provided **once** to generate the long lived token.

#### `LONG_LIVED_TOKEN`
**Leave this field empty.**

The application automatically exchanges the short-lived token for a long-lived token and stores it internally.  
You do **not** need to manually refresh or update this token.

#### `URL`
OAuth endpoint used to exchange access tokens.  
Default value is correct and should not be changed.

#### `IMGBB_API_KEY`
API key from https://api.imgbb.com  
Used to temporarily host images so Instagram can access them.


## Data directories

These paths control where images are read from and where used images are stored.

### `image_dir`
Directory containing images that are eligible for posting.

Example:
`./images`

### `used_image_dir`
Directory where images are moved after they have been posted.

Example:
`./posted`

Both paths can be absolute or relative to the project root.


## Settings

General behavior settings for the application.

### `deleteUsedPictures`
Controls what happens to images after posting.

- `true`  
  Images are **deleted** after they have been posted.

- `false`  
  Images are **deleted** after posting.

Recommended: set to `true` 

### `moveUsedPictures`
Controls what happens to images after posting.

- `true`  
  Images are **moved** after they have been posted.

- `false`  
  Images are remain in place after posting.

Recommended: set to `false` if you want to keep an archive of posted images.


