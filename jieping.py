#!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #Author: xiaomoren
# @Time    : 2018/2/13 9:50
from selenium import webdriver
import time

url = 'http://www.xxx.com'
def capture(url, save_fn="capture.png"):
    browser = webdriver.Chrome() # Get local session of firefox
    browser.set_window_size(1200, 900)
    browser.get(url) # Load page
    browser.execute_script("""
    (function () {
    var y = 0;
    var step = 100;
    window.scroll(0, 0);
    function f() {
    if (y < document.body.scrollHeight) {
    y += step;
    window.scroll(0, y);
    setTimeout(f, 50);
    } else {
    window.scroll(0, 0);
    document.title += "scroll-done";
    }
    }setTimeout(f, 1000);
    })();
    """)

    browser.save_screenshot(save_fn)
    browser.close()
# if __name__ == "__main__":
#     capture(url,save_fn='test.png')