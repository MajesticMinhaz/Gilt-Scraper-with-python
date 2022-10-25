<p align="center"><img src="https://img.shields.io/badge/Version-1.0.1-blue"></p>
<p align="center">
  <a href="https://github.com/mdminhaz2003">
    <img src="https://img.shields.io/github/followers/mdminhaz2003?label=Follow&style=social">
  </a>
  <a href="https://github.com/mdminhaz2003/Telegram-Scraper">
    <img src="https://img.shields.io/github/stars/mdminhaz2003/Telegram-Scraper?style=social">
  </a>
</p>
<p align="center" style="font-family: 'Fantasy';">
  www.gilt.com website scraper
</p>
<p align="center">
</p>

---

Requirements
============
* Python
* Google Chrome Browser
* Git

Install [Cookie Editor Extension](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) in your Google Chrome Browser
========

# Login to [gilt.com](https://www.gilt.com) with your Username and Password

## Follow instructions
### 1. Open gilt.com website in your browser
![1 Screenshot](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/images/1.png)
### 2. Open Cookie Editor Extension
![2 Screenshot](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/images/2.png)
### 3. Click on Export button to get all Cookie in JSON Format
![3 Screenshot](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/images/3.png)

## Paste your cookie data to [cookie.json](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/master/basic_files/cookie.json) file
```json
[
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1698151278,
        "hostOnly": false,
        "httpOnly": false,
        "name": "anon_client_id",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "3e3203ec-1bee-470a-955d-e6ca4365d74c"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1666680506,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_dv",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701659,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.currency",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "USD"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666621466.505275,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bm_sz",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "392A7707D89553ED867733618E998C14~YAAQVbxWaGnPuMaDAQAAYq2FCRGqhXsDgxrNeo4CmGkl8pADh/H+EZg33cgShQ/dmCZCpS2xcpS50FoFX7u7EpSDLSouhdh6UwZComVvnvm6rA+DEcxjVcwIJLPgR3o5p6Kz5jcH337KlwpARIyhdDYi7XQ11BuF7hG39LfT3CoURcM8vTvGfquPvp1/rfVGJapPi9JzCocihdWD1mqnkMgMHodDHCAkjoHkO8p/zf7EXOkv0Ggu2AQl5xwghrKt+ScAMwuk5WRGR5WRRQ3H/JHesRWdeKI8yWgMxX7FceefFpypAVE/QEpYWL6vGNC24Yjn9Jpn7Q2V~3617587~4535863"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1666617079.35595,
        "hostOnly": false,
        "httpOnly": false,
        "name": "user_segments_refresh",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "x"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1699069975.828141,
        "hostOnly": false,
        "httpOnly": false,
        "name": "schema",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "1:.www.gilt.com"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1698151263,
        "hostOnly": false,
        "httpOnly": false,
        "name": "riskified_session_id",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "YWI0NWFlYjYtNGQ5My00ODIyLWIwZWYtOTIyMGEyYjczZTFmOjE2NjY2MTUyNjM5MDI="
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666615320,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_gat_gtag_UA_44727658_31",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1701175279.355928,
        "hostOnly": false,
        "httpOnly": false,
        "name": "user_segments",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "\"WzksMzc2Myw2LDE1XQ==\""
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1698637985,
        "hostOnly": false,
        "httpOnly": false,
        "name": "cjConsent",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "MHxOfDB8Tnww"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175278.989811,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_ga",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "GA1.2.853678282.1664509983"
    },
    {
        "domain": ".gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "previous_country",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": true,
        "storeId": null,
        "value": "US"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701678,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.logLevel",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "ERROR"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1698151279,
        "hostOnly": false,
        "httpOnly": false,
        "name": "utag_main",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "v_id:01838c86aed1001f5cee6b28989b05065007805d00bd0$_sn:11$_ss:0$_st:1666617079397$dc_visit:11$job_id:138952$sub_id:142724609$list:23_HTML$original_link_id:9967694$BatchID:1210646$member_id:7318081$ses_id:1666615259665%3Bexp-session$_pn:3%3Bexp-session$dc_event:9%3Bexp-session$dc_region:ap-east-1%3Bexp-session"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "browsable_segments",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "WzM3NjNd"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1701175278.983219,
        "hostOnly": true,
        "httpOnly": false,
        "name": "_attn_",
        "path": "/",
        "sameSite": "strict",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "eyJ1Ijoie1wiY29cIjoxNjY0NTA5OTg1Mzk1LFwidW9cIjoxNjY0NTA5OTg1Mzk1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQ3NmQ5NmVlMjlkODRiYmFiMmFhZmU2MTQwMmVhNjMzXCJ9In0="
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666622457.355994,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bm_sv",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "B81B089A77EC6A8A48120D4669512A91~YAAQrydzaNRpx/mDAQAA7P4CChEc/dUeWOKeqMCgMWQSw+Os+u/WMWljURsgHK5wL+SI8Kmow9LD+QdO8uKr8Gv5mfvC3OYlgPqLQ04HKtOTKn4AE/zNl8wMKzk3aEhr2C8ozhevS3x5e1aGS7A3k0C5zzAUtc3dnHIvxzI8T5KLsBXPjXeGG7J1KjiRIP5b/nTswqLhEk401Btylq1Taspl+b3UKxlgyMI9FpwPOdggUmyCzmQes68GjYN6gyA=~1"
    },
    {
        "domain": ".gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "__attentive_client_user_id",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": true,
        "storeId": null,
        "value": "86743629"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "location_segment",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "NDc0OA=="
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1696045980,
        "hostOnly": false,
        "httpOnly": false,
        "name": "BI.visitorId",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "01838c86aed1001f5cee6b28989b05065007805d00bd0"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175280.96896,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_evga_c7fb",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "b81d500f94991878.0DT"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666680535,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.lcpRuleId",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": ""
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175278.80071,
        "hostOnly": false,
        "httpOnly": false,
        "name": "__cuid",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "159d4af8b87249a99bcc5fd8f228efa3"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666680554,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.country",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "US"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701678,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.isInternational",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "false"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1700743278,
        "hostOnly": false,
        "httpOnly": false,
        "name": "cjUser",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "28180a9e-3baf-45b7-8e21-b5b1d312ed00"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1674391279,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_fbp",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "fb.1.1664509982499.1940105367"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1666616178,
        "hostOnly": true,
        "httpOnly": false,
        "name": "_dd_s",
        "path": "/",
        "sameSite": "strict",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "rum=0&expire=1666616178751"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1701175278.284101,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ciosec",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "2b6efdd37bda2551b53aff79e0edb5478450db22646defde7bfcc318026db6fa"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666621727.893822,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bm_mi",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "52A7C92F6C3D1A74FE5E02CF2AAAA56B~YAAQrydzaC1mx/mDAQAAFKsCChGv+mbJjkigS3oI3J13x+5VI2zio5SkQj67vDD5PQloA0m1F+3LikOTNQQWiuQqzDUp8ZihudS0F1FX+3uixn+DWGTox99si0UgoHAt8UPK8xdm8kuOo7cTb7gBRWVc0htcCyafIX/oPq3inpVUw1VYr4bZ6fwQxMtZ7SIBRFwiSuJoZdJcl4qn29dKiRcJ+PCiUZz4h8PcqNmtZY94l7vZ9RrZJHHjPLvbaPzKn26TFtJWpJiqJSwd6H7lzVkflHUZYQRsL41sg8F9tizC7x+zT4u9kjtC/B5xAmx02cfEmLM=~1"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1696045977,
        "hostOnly": false,
        "httpOnly": false,
        "name": "BI.maxTouchPoints",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "0"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701678,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.env",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "PROD"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "geolocation_data",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "{\"continent\":\"AS\",\"timezone\":\"GMT+6\",\"country\":\"BD\",\"city\":\"DHAKA\",\"lat\":\"23.72\",\"long\":\"90.41\"}"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1666617078,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_creativeFilter",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "\"IS_NOT_NEW_MEMBER\""
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1699069987.059296,
        "hostOnly": true,
        "httpOnly": false,
        "name": "cbt-consent-banner",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "CROSS-BORDER%20Consent%20Banner"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "user_data",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "\"eyJiYWdfY291bnQiOjAsImNyZWRpdHMiOiIkMC4wMCIsImZpcnN0TmFtZSI6IiIsImVtYWlsIjoiaGlsZnVsZnV6dWxvcmdhbml6YXRpb245QGdtYWlsLmNvbSIsImlzU3RhZmYiOmZhbHNlLCJwdXJsIjoiaGlsZnVsZnV6dWxvcmciLCJpc0F1dGhlbnRpY2F0ZWQiOnRydWUsInJ1ZTFfYXBwX2lkIjoiODY3NDM2MjkiLCJnZW5kZXIiOiJNIiwiam9pbkRhdGUiOjE2NjQ1MDk3MjQsImhhc1ByZWZlcnJlZEFkZHJlc3MiOmZhbHNlLCJoYXNQcmVmZXJyZWRDYXJkIjpmYWxzZSwiaGFzTW9iaWxlTnVtYmVyIjpmYWxzZSwicmVwZWF0QnV5ZXIiOmZhbHNlLCJoYXNSdWUzNjUiOjAsImhhc1J1ZTMwIjowfQ==\""
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701678,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.apiKey",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "391dd480-dddc-11e8-9307-cb3b61fd3dda"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "default_segments",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "WzksNl0="
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1701175278.284055,
        "hostOnly": false,
        "httpOnly": false,
        "name": "remember_me_cookie",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "\"hilfulfuzulorganization9@gmail.com:1981993278:1c3ac19b8f6525bed523b0c7a77889c659f819bd\""
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1700779279,
        "hostOnly": false,
        "httpOnly": false,
        "name": "cto_bundle",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "bdOcC19ybnJLbDExbDQ2TzV4ZHNqOGhaaldoMUtVNzlDeGNMUURBSlYwWDJjYmJFQjl0M0IzNzd3VE9SbHFublRQcWpBN1pPSFhwODZJWUxudTgyV0UwJTJGWUJYbndSM1BIbDV6RVRLRFJsY0xyOG9MbnowbThPZTV4VnFsakZxNmgwUWVsbCUyQmpMSndPSkxUUGNnbWRJTkwzdnRnJTNEJTNE"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1667102018.029774,
        "hostOnly": false,
        "httpOnly": false,
        "name": "visited",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "\"\""
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1699069985.386913,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_cco",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1664509985386"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1701175278.998296,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_id",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "476d96ee29d84bbab2aafe61402ea633"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1666617078,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_pv",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "3"
    },
    {
        "domain": "www.gilt.com",
        "expirationDate": 1666617063,
        "hostOnly": true,
        "httpOnly": false,
        "name": "__attentive_ss_referrer",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "\"ORGANIC\""
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1698151279.409935,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_abck",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "5141BEC1D4F926D54F405DDBCA1AD947~0~YAAQrydzaNppx/mDAQAAIv8CCgiezWhumLGH3DWIxy7564JsW6EGvjd49Ai8Nrp3aHP2HBBu/iJcaWW9E1epExmb/pqDt4S9ai+W5RkUMnyFvXL7qn6JHGeGgv8Lj0rqbqBIJ4TQF65HdzeZWyzn/4UZDpHnfRWOqYkOYhf1t0PtnyYEqSmELXXW3hWqYkLN5LpRsmuwURLxrFK5hHZf1gQcC90rLvIhMwb5Wpu/iz6KOl+mx4yaACb9mNcjtQ/oqdjGe9wTcnkNHP4Egyjb5HyHwkYcjxRouaUxQIP8qM6TQw2RDxwy9qpCFI1S5YqDhj02kgUzc11sFEOnFKJkWMd/WNetiVmon2sy0g+/TbI+7kGpCuOyZsBr+w==~-1~-1~-1"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666617079,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_evgn_c7fb",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "%7B%22puid%22%3A%225ZRIry37ILDZf2O_i3hoEQ6-lE1Db3it87MqZ7s_pzU%22%7D"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1672285981,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_gcl_au",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1.1.301101988.1664509982"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701678,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_gid",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "GA1.2.1499086804.1666594104"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175278.940882,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_lc2_fpi",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "d7613dab5864--01ge68dg22cgg78xn0ewgf6qxd"
    },
    {
        "domain": ".gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "_li_dcdm_c",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": true,
        "storeId": null,
        "value": ".gilt.com"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666621727.771935,
        "hostOnly": false,
        "httpOnly": true,
        "name": "ak_bmsc",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "5DF639A60E68E19A537496043C87780E~000000000000000000000000000000~YAAQrydzaJpmx/mDAQAAa7ICChHjOibRo7IN0UxHfy23Uj/YgDVid1InB3Eqxt+DUDiHY3Kg3KtgfpC6r6HMHpvUJPiXxCQn4tcC/mUe8BdYgLhGHPt2DcsJDoQ9tUjia687i6TYBffx7i8uZZiJ6TQrtzblNXezfthoW9OGUMfixEtvwfVEc+ibkw6J8QbKGacYqhMCxuhx7vssbhark/V6bO17DIQJZZ7tMOVZV/6gqJHSGc+HHP/b40zAo8mX2k/mWS35fW15IgerWBNU0o1yflhg8BFWXD2SYnhhvDWfN7L5C3n8qeWv4dkULrGIPtFMwpRGStNIxi/Dh5KKIsu5xJzu1D/O3f+Adk+Zdo5WHwA5OH36uNmHVchCSYSANZFSXGBeES4mNeCwqZjTQgN/a/UgV+Lhjco="
    },
    {
        "domain": "www.gilt.com",
        "hostOnly": true,
        "httpOnly": false,
        "name": "attntv_mstore_email",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "hilfulfuzulorganization9@gmail.com:0"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666680535,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.currencyQuoteId",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "81161381"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666701659,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.language",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "bn"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1666680501,
        "hostOnly": false,
        "httpOnly": false,
        "name": "bfx.sessionId",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "c4837daf-4dc7-44db-9bf8-96e75fe140e9"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1698151259,
        "hostOnly": false,
        "httpOnly": false,
        "name": "BI.sessionId",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "1666615259665"
    },
    {
        "domain": ".www.gilt.com",
        "expirationDate": 1698064878.284224,
        "hostOnly": false,
        "httpOnly": false,
        "name": "csrftoken",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "XGQ9S572voaWWJtO5xPSKSnJmzemQ6UN"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "edr_score",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "-5"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175278.827676,
        "hostOnly": false,
        "httpOnly": false,
        "name": "lastRskxRun",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1666615278826"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175280.350448,
        "hostOnly": false,
        "httpOnly": false,
        "name": "rCookie",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "oe3rms1kn08tc915o8lrzfl8ny9jos"
    },
    {
        "domain": ".gilt.com",
        "expirationDate": 1701175278.828552,
        "hostOnly": false,
        "httpOnly": false,
        "name": "rskxRunCookie",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "0"
    },
    {
        "domain": "www.gilt.com",
        "hostOnly": true,
        "httpOnly": false,
        "name": "session-page-view",
        "path": "/boutique",
        "sameSite": null,
        "secure": false,
        "session": true,
        "storeId": null,
        "value": "1"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": true,
        "name": "sessionid",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "mk3eaeldwycl8r8vz0ta8mgvmbws61np"
    },
    {
        "domain": ".www.gilt.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "user_agent_set",
        "path": "/",
        "sameSite": null,
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "desktop"
    }
]
```
Build
=====
To build and run this application locally, you'll need the latest versions of Git, Google Chrome Browser and Python From your command line:

### Clone this repository
```commandline
git clone https://github.com/mdminhaz2003/Gilt-Scraper-with-python.git
```

### Go into the repository
```commandline
cd Gilt-Scraper-with-python
```
### .env file structure
```text
BASE_URL=https://www.gilt.com/boutique/         # Base path should not be changed.
PAGE_URL=https://www.gilt.com/nav/men/clothing/activewear%20&%20loungewear?click_source=Site+Section+Navbar&dsi=CAT-2140890951--a05a52ab-faee-40e5-b7b1-8b9f2dae1289&lsi=a6601dea-c3ec-4501-983c-526d4fd4f4b2&page={}     # Enter your page url here and remove Page number and replace it to "{}"
START_PAGE=1    # Page start
END_PAGE=3      # Page End

DRIVER_PATH=./chrome_driver/Linux_64/chromedriver   # Enter your chrome driver path for Mac or Linux

OUTPUT_CSV_PATH=./output_csv/gilt_product_info.csv  # Enter your output CSV file path
PRODUCT_URL_DB_PATH=./db_files/gilt_product_url.json
PRODUCT_INFO_DB_PATH=./db_files/gilt_product_info.json
COOKIE_PATH=./basic_files/cookie.json
```
### Requirements installing
```commandline
python3 -m pip install -r requirements.txt
```
### Scrap only product URL
```commandline
python3 gilt_url_scraper.py
```
### Scrap Product Details
```commandline
python3 gilt_product_scraper.py
```
### Finally, we will get a JSON file [./db_files/gilt_product_info.json](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/db_files/gilt_product_info.json)

### Convert JSON to CSV Format
```command
python3 json_to_csv_converter.py
```
### Now, we will get a csv file in [.output_csv/gilt_product_info.csv](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/output_csv/gilt_product_info.csv)

# [LICENSE](https://github.com/mdminhaz2003/Gilt-Scraper-with-python/blob/version_1.0.1/output_csv/gilt_product_info.csv)
```text
The MIT License (MIT)

Copyright (c) 2022 MD. MINHAZ

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

[Connect with Author](https://www.github.com/mdminhaz2003/)
========

<p align="center">
    <a href="https://www.buymeacoffee.com/mdminhaz2003"><img src="https://img.shields.io/badge/-Buy me a coffee-000000?style=for-the-badge&logo=buymeacoffee&logoColor=yellow"/></a>
    <a href="https://www.youtube.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-FF0000?style=for-the-badge&logo=YouTube&logoColor=white"/></a>
    <a href="https://www.facebook.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-3423A6?style=for-the-badge&logo=Facebook&logoColor=white"/></a>
    <a href="https://www.linkedin.com/in/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white"/></a>
    <a href="mailto:mdm047767@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=for-the-badge&logo=Gmail&logoColor=white"/></a>
    <a href="https://instagram.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-E4405F?style=for-the-badge&logo=Instagram&logoColor=white"/></a>
    <a href="https://twitter.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
</p>
