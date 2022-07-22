package com.xbzxit.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.List;

/**
 * @author xbzxit
 * @version 1.0
 * @create 2022-07-21-14:15
 * @company www.xbzxit.com
 */

public class SeleniumElementPositionTest {

    public static void main(String[] args) throws InterruptedException {
        WebDriver driver;
        //System.setProperty("webdriver.firefox.marionette","E:\\DevelopmentServer\\WebDriver\\bin\\geckodriver.exe");
        System.setProperty("webdriver.firefox.bin","E:\\Program Files\\Mozilla Firefox\\firefox.exe");
        driver = new FirefoxDriver();
        driver.get("http://www.imooc.com/user/newlogin/from_url");

        driver.findElement(By.tagName("input")).sendKeys("xbzxit@163.com");
        driver.findElement(By.name("password")).sendKeys("");
        driver.findElement(By.xpath("//*[@id=\"auto-signin\"]")).click();
        driver.findElement(By.id("auto-signin")).click();

        //快速注册
        //region 定位span元素
        // <div class="pop-login-signup-box clearfix">
        //      <span data-fromto="signin:signup" class="xa-showSignup">快速注册</span>
        // </div>
        //方式一
        //driver.findElement(By.xpath("//div[@class='pop-login-signup-box clearfix']/span")).click();
        //方式二
        //driver.findElement(By.xpath("//span[contains(text(),'快速注册')]")).click();
        //方式三
        //driver.findElement(By.xpath("/html/body/div[2]/div/div/div[3]/div[1]/span")).click();
        //方式四
        driver.findElement(By.className("xa-showSignup")).click();
        //endregion
        //返回账号登录
        driver.findElement(By.className("xa-showSignin")).click();

        driver.findElement(By.tagName("input")).sendKeys("xbzxit@163.com");
        driver.findElement(By.name("password")).sendKeys("");
        driver.findElement(By.className("moco-btn-red")).click();
        driver.manage().window().maximize();

        // 重定向后，等会的 session就没了
        driver.get("http://www.imooc.com");
        driver.findElement(By.className("imv2-search2")).click();
        driver.findElement(By.className("search-input")).sendKeys("java", Keys.ENTER);
        WebElement element = driver.findElement(By.className("nav-item"));
        List<WebElement> elements = element.findElements(By.tagName("li"));

        elements.get(3).click();

    }

}