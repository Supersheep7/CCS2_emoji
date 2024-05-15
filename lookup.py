import pandas as pd 

root = {
    "😂": {
        "name": "lol",
        "unicode": "U0001F602",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 54438
    },
    "❤️": {
        "name": "red-heart",
        "unicode": "U00002764",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 44028
    },
    "🤣": {
        "name": "rofl",
        "unicode": "U0001F923",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 40534
    },
    "👍": {
        "name": "thumbs-up",
        "unicode": "U0001F44D",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 27475
    },
    "😭": {
        "name": "crying-face",
        "unicode": "U0001F62D",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 49274
    },
    "🙏": {
        "name": "amen",
        "unicode": "U0001F64F",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 36096
    },
    "😘": {
        "name": "blowing-kiss",
        "unicode": "U0001F618",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 7304
    },
    "🥰": {
        "name": "happy-love",
        "unicode": "U0001F970",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 29805
    },
    "😍": {
        "name": "crazy-love",
        "unicode": "U0001F60D",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 29616
    },
    "😊": {
        "name": "happy-smile",
        "unicode": "U0001F60A",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 9389
    },
    "🎉": {
        "name": "party",
        "unicode": "U0001F389",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 22185
    },
    "😁": {
        "name": "beaming",
        "unicode": "U0001F601",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 6082
    },
    "💕": {
        "name": "couple-hearts",
        "unicode": "U0001F495",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 8379
    },
    "🥺": {
        "name": "oww",
        "unicode": "U0001F97A",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 6878
    },
    "😅": {
        "name": "ehm",
        "unicode": "U0001F605",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": 25706
    },
    "🔥": {
        "name": "fire-emoji",
        "unicode": "U0001F525",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤦": {
        "name": "facepalm",
        "unicode": "U0001F926",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤷": {
        "name": "dunno",
        "unicode": "U0001F937",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙄": {
        "name": "ehh",
        "unicode": "U0001F644",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😆": {
        "name": "top-kek",
        "unicode": "U0001F606",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤗": {
        "name": "hugging-face",
        "unicode": "U0001F917",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😉": {
        "name": "wink",
        "unicode": "U0001F609",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🎂": {
        "name": "bday",
        "unicode": "U0001F382",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤔": {
        "name": "mumble",
        "unicode": "U0001F914",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👏": {
        "name": "grats",
        "unicode": "U0001F44F",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙂": {
        "name": "smile",
        "unicode": "U0001F642",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😳": {
        "name": "omg",
        "unicode": "U0001F633",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🥳": {
        "name": "party-hat",
        "unicode": "U0001F973",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😎": {
        "name": "sunglasses",
        "unicode": "U0001F60E",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👌": {
        "name": "ok",
        "unicode": "U0001F44C",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💜": {
        "name": "purple-heart",
        "unicode": "U0001F49C",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😔": {
        "name": "bit-sad",
        "unicode": "U0001F614",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💪": {
        "name": "muscle",
        "unicode": "U0001F4AA",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "✨": {
        "name": "bling",
        "unicode": "U00002728",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💖": {
        "name": "heart-bling",
        "unicode": "U0001F496",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👀": {
        "name": "eyes",
        "unicode": "U0001F440",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😢": {
        "name": "tear",
        "unicode": "U0001F622",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👉": {
        "name": "point-right",
        "unicode": "U0001F449",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😩": {
        "name": "augh",
        "unicode": "U0001F629",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💯": {
        "name": "100",
        "unicode": "U0001F4AF",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌹": {
        "name": "rose",
        "unicode": "U0001F339",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🎈": {
        "name": "balloon",
        "unicode": "U0001F388",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😡": {
        "name": "rage",
        "unicode": "U0001F621",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💐": {
        "name": "flowers",
        "unicode": "U0001F490",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙈": {
        "name": "monkey-eyes",
        "unicode": "U0001F648",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤞": {
        "name": "fingers-crossed",
        "unicode": "U0001F91E",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙌": {
        "name": "hands-up",
        "unicode": "U0001F64C",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤪": {
        "name": "silly",
        "unicode": "U0001F92A",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💋": {
        "name": "kiss",
        "unicode": "U0001F48B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💀": {
        "name": "og",
        "unicode": "U0001F480",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💔": {
        "name": "broken-heart",
        "unicode": "U0001F494",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤩": {
        "name": "eye-stars",
        "unicode": "U0001F929",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙃": {
        "name": "topsy",
        "unicode": "U0001F643",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😱": {
        "name": "scared",
        "unicode": "U0001F631",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😴": {
        "name": "sleepy",
        "unicode": "U0001F634",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌞": {
        "name": "sunny-face",
        "unicode": "U0001F31E",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌸": {
        "name": "pink-flower",
        "unicode": "U0001F338",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😈": {
        "name": "devilish",
        "unicode": "U0001F608",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🎶": {
        "name": "music",
        "unicode": "U0001F3B6",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🎊": {
        "name": "confetti",
        "unicode": "U0001F38A",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "☀️": {
        "name": "sun",
        "unicode": "U00002600",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💰": {
        "name": "money-bag",
        "unicode": "U0001F4B0",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👑": {
        "name": "crown",
        "unicode": "U0001F451",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🎁": {
        "name": "gift",
        "unicode": "U0001F381",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💥": {
        "name": "explosion",
        "unicode": "U0001F4A5",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙋": {
        "name": "hand-raised",
        "unicode": "U0001F64B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😑": {
        "name": "plain-face",
        "unicode": "U0001F611",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🥴": {
        "name": "drunk",
        "unicode": "U0001F974",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💩": {
        "name": "bozhi",
        "unicode": "U0001F4A9",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "✅": {
        "name": "good",
        "unicode": "U00002705",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤮": {
        "name": "puke",
        "unicode": "U0001F92E",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌟": {
        "name": "star",
        "unicode": "U0001F31F",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "❗": {
        "name": "exclamation",
        "unicode": "U00002757",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌈": {
        "name": "pride",
        "unicode": "U0001F308",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🖕": {
        "name": "fuck-you",
        "unicode": "U0001F595",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🔴": {
        "name": "red-dot",
        "unicode": "U0001F534",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌻": {
        "name": "sunflower",
        "unicode": "U0001F33B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💃": {
        "name": "flamenco",
        "unicode": "U0001F483",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🏃": {
        "name": "running-man",
        "unicode": "U0001F3C3",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👁️": {
        "name": "eye",
        "unicode": "U0001F441",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "⚡": {
        "name": "bolt",
        "unicode": "U000026A1",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "☕": {
        "name": "coffee",
        "unicode": "U00002615",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍀": {
        "name": "clover",
        "unicode": "U0001F340",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💦": {
        "name": "spurt",
        "unicode": "U0001F4A6",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🦋": {
        "name": "butterfly",
        "unicode": "U0001F98B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😹": {
        "name": "cat-laughing",
        "unicode": "U0001F639",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💤": {
        "name": "zzz",
        "unicode": "U0001F4A4",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🐰": {
        "name": "bunny",
        "unicode": "U0001F430",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍻": {
        "name": "cheers",
        "unicode": "U0001F37B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤠": {
        "name": "cowboy",
        "unicode": "U0001F920",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "😻": {
        "name": "crazy-love-cat",
        "unicode": "U0001F63B",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌙": {
        "name": "crescent",
        "unicode": "U0001F319",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🙊": {
        "name": "monkey-mouth",
        "unicode": "U0001F64A",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤡": {
        "name": "clown",
        "unicode": "U0001F921",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤓": {
        "name": "glasses",
        "unicode": "U0001F913",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "☠️": {
        "name": "brook",
        "unicode": "U0002620F",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🥶": {
        "name": "freeze",
        "unicode": "U0001F976",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍆": {
        "name": "mulignan",
        "unicode": "U0001F619",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🤑": {
        "name": "dollar-eyes",
        "unicode": "U0001F911",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💅": {
        "name": "nails",
        "unicode": "U0001F485",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🐶": {
        "name": "doggo",
        "unicode": "U0001F436",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍓": {
        "name": "strawberry",
        "unicode": "U0001F353",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "👄": {
        "name": "lips",
        "unicode": "U0001F444",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌿": {
        "name": "branch",
        "unicode": "U0001F33F",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "➡️": {
        "name": "go-right",
        "unicode": "U000027A1",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍑": {
        "name": "peach",
        "unicode": "U0001F351",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "💎": {
        "name": "diamond",
        "unicode": "U0001F48E",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🌱": {
        "name": "sprout",
        "unicode": "U0001F331",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "⚠️": {
        "name": "warning",
        "unicode": "U000026A0",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    },
    "🍷": {
        "name": "wine",
        "unicode": "U0001F377",
        "visual_features": None,
        "embedding": None,
        "mixed_features": None,
        "dataset_count": None
    }
}

df = pd.DataFrame(root).T

print(df.head())