# Web 200-1 - Gifting a White Elephant
## Description
Ok, everyone, I've got a really cool challenge for this one but I need everyone to not rat me out. For this challenge, I've decided to put you in the shoes of an investigator looking to take down a website that hosts illegal content. In this case, a forum that posts carding data. Your task is to probe the site for evidence and identify every subject.

I wanted this to be as real as possible, so I've got hundreds of users, dozens of moderators, and the kingpin site administrator. I've got dozens of pages, hundreds of clues, and it's a full multimedia site. Which is why I need you to be cool about this and not go blabbing about this challenge, because in order to make the scenario as real as possible I'm using real data from real cases. I realize that this is, technical speaking, mega-illegal, but I wanted a cool challenge. I guess I could have created simulated evidence, but... eh... Sounds like a lot of work and to be honest I'm just over it. It's whatever, just keep it to yourself and it'll be fine.

[34.135.223.176 port 6007](http://34.135.223.176:6007/)

## Solution
In the source file, there is a reference to the endpoint `/agent-access`.

When visiting this page, an access denied page is shown. We also see JS console logs indicating how the user is authorized. 
Make a GET request with the correct `User-Agent` header: `FBI-SiteAccess-Authorized-Agent`.

## Flag
`poctf{uwsp_4_fr13nd_70_4ll}`
