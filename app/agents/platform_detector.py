def detect_platform(state):

    url = state.get("apply_url", "").lower()

    platform = "unknown"
    auto_apply_supported = False

    if "gh_jid" in url:
        platform = "greenhouse"
        auto_apply_supported = True

    elif "greenhouse" in url:
        platform = "greenhouse"
        auto_apply_supported = True

    elif "lever.co" in url:
        platform = "lever"
        auto_apply_supported = True

    elif "workdayjobs" in url:
        platform = "workday"
        auto_apply_supported = True

    elif "ashbyhq" in url:
        platform = "ashby"
        auto_apply_supported = True

    elif "google.com/forms" in url:
        platform = "google_form"
        auto_apply_supported = True

    return {
        **state,
        "platform": platform,
        "auto_apply_supported": auto_apply_supported
    }

    