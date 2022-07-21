package com.xbzxit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * @author xbzxit
 * @version 1.0
 * @create 2022-07-20-21:46
 * @company www.xbzxit.com
 */

public class demo {

    public static void main(String[] args) {
        WebDriver driver;
        //System.setProperty("webdriver.firefox.bin","E:\\Program Files\\Mozilla Firefox\\firefox.exe");
        System.setProperty("webdriver.chrome.bin","\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"");

        //driver = new FirefoxDriver();
        driver = new ChromeDriver();

        driver.get("http://www.baidu.com");



    }



}