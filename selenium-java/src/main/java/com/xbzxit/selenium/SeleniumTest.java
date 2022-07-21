package com.xbzxit.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * @author xbzxit
 * @version 1.0
 * @create 2022-07-21-14:15
 * @company www.xbzxit.com
 */

public class SeleniumTest {

    public static void main(String[] args) {
        WebDriver driver;
        System.setProperty("webdriver.firefox.marionette","E:\\DevelopmentServer\\WebDriver\\bin\\geckodriver.exe");
        //System.setProperty("webdriver.firefox.bin","E:\\Program Files\\Mozilla Firefox\\firefox.exe");
        //System.setProperty("webdriver.chrome.bin","\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"");

        driver = new FirefoxDriver();
        //driver = new ChromeDriver();

        driver.get("http://www.baidu.com");
    }

}