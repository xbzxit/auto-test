package com.xbzxit.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * Span元素的定位
 *
 * @author xbzxit
 * @version 1.0
 * @create 2022-07-21-15:21
 * @company www.xbzxit.com
 */

public class SeleniumSpan {

    public static void main(String[] args) {
        WebDriver driver;
        System.setProperty("webdriver.firefox.bin","E:\\Program Files\\Mozilla Firefox\\firefox.exe");
        driver = new FirefoxDriver();
        driver.get("https://www.baidu.com/");
        WebElement div = driver.findElement(By.cssSelector("span.tools span :nth-child(1)"));
        WebElement div2 = driver.findElement(By.cssSelector("span#mHolder :nth-child(1)"));
        WebElement span1 = driver.findElement(By.cssSelector("span.tools"));
        WebElement span2 = driver.findElement(By.cssSelector("span.tools span"));
        WebElement span3 = driver.findElement(By.cssSelector("#mCon span"));

        System.out.println("使用索引定位" + div.getAttribute("outerHTML"));
        System.out.println("使用索引定位" + div2.getAttribute("outerHTML"));

        System.out.println("使用索引定位" + span1.getAttribute("outerHTML"));
        System.out.println("使用索引定位" + span2.getAttribute("outerHTML"));
        System.out.println("使用索引定位" + span3.getAttribute("outerHTML"));

    }

}