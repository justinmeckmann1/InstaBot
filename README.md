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
        "image_dir": "./images/post",
        "used_image_dir": "./images/posted",
        "corrupted_image_dir": "./images/corrupted"
    },
    "settings": {
        "deleteUsedPictures": false,
        "moveUsedPictures": true,
        "maxAttempts": 5
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

This token must be provided **once** to generate the long-lived token.

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

---

## Data directories

These paths control where images are read from, where used images are stored, and where corrupted files are moved.

### `image_dir`
Directory containing images that are eligible for posting.

Default:
`./images/post`

### `used_image_dir`
Directory where images are moved after they have been posted (if enabled).

Default:
`./images/posted`

### `corrupted_image_dir`
Directory where invalid/corrupted images are moved when the bot detects a problem (e.g. unreadable file, unsupported format, repeated upload failures).

Default:
`./images/corrupted`

All paths can be absolute or relative to the project root.

---

## Settings

General behavior settings for the application.

### `deleteUsedPictures`
This is not yet implemented! All images are moved to corrupted or posted

Controls whether successfully posted images are deleted after posting.

- `true`  
  Images are **deleted** after they have been posted.

- `false`  
  Images are **not deleted** after posting.

Recommended: keep `false` if you want an archive.
---

### `moveUsedPictures`
Controls whether successfully posted images are moved after posting.

- `true`  
  Images are **moved** to `used_image_dir` after they have been posted.

- `false`  
  Images **remain** in `image_dir` after posting.

Recommended: set to `true` if you want a clean post folder.

---

### `maxAttempts`
Controls how many times InstaBot will retry processing/posting an image before treating it as failed.

- Example: `5`  
  The bot retries up to 5 times before giving up. After that, the image may be moved to `corrupted_image_dir`.

Recommended: `5` is a good default.
