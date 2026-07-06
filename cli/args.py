import sys
from utils import logger


def parse() -> dict:
    argv = sys.argv[1:]

    if not argv:
        logger.warn("No Arguments Provided, Please Read The Following")
        logger.info("Make Sure Your Phone Is Plugged In Via USB Cable")
        logger.info("Make Sure WhatsApp Is Open On The Username Key Page")
        logger.info("Run python bot.py --help To See All Available Commands")
        raise SystemExit(0)

    if "--help" in argv:
        from cli.help import show_help
        show_help()
        raise SystemExit(0)

    targets = []
    save_ss = False
    inline = True

    for arg in argv:
        if arg == "--ss":
            save_ss = True
        elif arg == "--twin":
            targets += [str(i) * 4 for i in range(10)]
        elif arg == "--no-inline":
            inline = False
        elif arg.startswith("--") and arg[2:].isdigit() and len(arg[2:]) == 4:
            targets.append(arg[2:])

    targets = list(dict.fromkeys(targets))

    if not targets:
        logger.error("No Valid Target Keys Provided, Use --help For Usage")
        raise SystemExit(1)

    return {
        "targets": targets,
        "save_ss": save_ss,
        "inline": inline,
    }
