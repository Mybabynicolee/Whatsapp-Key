from vision.capture.screenshot import take, take_and_save
from vision.ocr.parser import read_key, find_button, find_save_button, find_generate_button
from device.interaction.input import tap
from device.interaction.screen import cleanup
from utils import logger

_btn_generate = None
_btn_save = None


def search_loop(targets: set, save_ss: bool, result_holder: list, stop_event):
    global _btn_generate, _btn_save

    while not stop_event.is_set():
        img = take()
        if img is None:
            logger.warn("Screen Capture Failed, Retrying Next Attempt")
            continue

        key = read_key(img)
        if not key:
            logger.warn("Key Not Detected In Current Frame")
            if _btn_generate:
                tap(*_btn_generate)
            else:
                pos = find_button(img, "get a different key") or find_generate_button(img)
                if pos:
                    _btn_generate = pos
                    tap(*pos)
                else:
                    logger.warn("Generate Button Not Found In Frame")
            continue

        # print detected key inline (replaces previous line)
        logger.info_inline(f"Key Detected: {key}")

        if key in targets:
            # ensure we end inline output and go to a fresh line for final messages
            print()

            stop_event.set()
            result_holder.append(key)
            if save_ss:
                take_and_save(key)
            if _btn_save is None:
                _btn_save = find_button(img, "save key") or find_save_button(img)
            if _btn_save:
                tap(*_btn_save)
            else:
                logger.warn("Save Button Not Found, Skipping Tap")

            logger.info(f"Target Key Found And Saved {key}")
            cleanup()
            return

        if _btn_generate:
            tap(*_btn_generate)
        else:
            pos = find_button(img, "get a different key") or find_generate_button(img)
            if pos:
                _btn_generate = pos
                tap(*pos)
            else:
                logger.warn("Generate Button Not Found In Frame")
