# Line Rich Menu Uploader
---

This is an small gist I think it would help some Line Developpers. Feel free to fork and make pull request if there's any improvement you wanna make or you think it should improved :)

**Usage:**
Create and upload rich menu using Line API.

1. Use [Line Bot Designer](https://developers.line.biz/en/services/bot-designer/) to generate json for each rich menu
2. Create `.env` file and put `LINE_ACCESS_TOKEN` inside that file
3. Edit `template.json` with following conventions:
    - Use `filename` WITHOUT extension as a key
    - Use json generated from Line Bot Designer as a value
3. [Optional] Specify image directory and output file name
4. Edit runner (last line) according to your needs
5. Run `python rich_maker.py`

## References
--
- [Rich Menu Object](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)