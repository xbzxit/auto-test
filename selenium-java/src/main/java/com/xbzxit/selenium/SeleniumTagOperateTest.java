package com.xbzxit.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;
import java.util.Set;
import java.util.concurrent.TimeUnit;

/**
 * Input标签的常见操作
 * @author xbzxit
 * @version 1.0
 * @create 2022-07-22-8:59
 * @company www.xbzxit.com
 */

public class SeleniumTagOperateTest {

    public WebDriver driver;
    public String windowsHandle;

    /**
     * 初始化浏览器驱动
     */
    public void InitDriver() {

        System.setProperty("webdriver.firefox.bin","E:\\Program Files\\Mozilla Firefox\\firefox.exe");
        driver = new FirefoxDriver();
        driver.get("http://www.imooc.com/user/newlogin/from_url");
        driver.manage().window().maximize();
    }

    /**
     * input 操作
     */
    public void inputBox() {
        //sendKeys 设置输入内容
        driver.findElement(By.name("email")).sendKeys("123456@qq.com");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        //clear 将输入的内容清空
        driver.findElement(By.name("email")).clear();
        //getAttribute 获取指定属性的值
        String str = driver.findElement(By.name("email")).getAttribute("placeholder");
        System.out.println("placeholder=" + str);
    }

    /**
     * 单选按钮 操作
     */
    public void radioBox() {
        driver.get("http://www.imooc.com/user/setprofile");
        driver.findElement(By.className("pull-right")).click();
        List<WebElement> elements = driver.findElements(By.xpath(".//*[@id='profile']/div[4]/div/label//input"));
        System.out.println(elements.size());

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for (WebElement radio : elements) {
            boolean flag = radio.isSelected();
            if (!flag) {
                radio.click();
            } else {
                System.out.println("selected");
            }
        }
    }

    /**
     * 复选框操作
     */
    public void checkBox() {
        WebElement check =  driver.findElement(By.id("auto-signin"));
        System.out.println("是否选中" + check.isSelected());
        System.out.println("是否有效" + check.isEnabled());

        check.clear();

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        check.click();
    }

    /**
     * 按钮
     */
    public void button() {
        WebElement login = driver.findElement(By.className("btn-red"));
        System.out.println("是否选中" + login.isSelected());
        System.out.println("是否有效" + login.isEnabled());
        login.click();
    }

    /**
     * form表单
     */
    public void webForm() {
        driver.findElement(By.id("signup-form")).submit();
    }

    /**
     * 文件上传表单
     */
    public void upHeader() {
        driver.get("http://www.imooc.com/user/setbindsns");
        this.sleep(2000);
        String jsStr = "document.getElementsByClassName('update-avator')[0].style.bottom='0'";
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript(jsStr);
        this.sleep(2000);

        driver.findElement(By.className("js-avator-link")).click();
        driver.findElement(By.id("upload")).sendKeys("D:\\a.jpg");

    }

    /**
     * 下拉框操作
     */
    public void downSlectBox() {
        driver.get("http://www.imooc.com/user/setprofile");
        driver.findElement(By.className("pull-right")).click();
        this.sleep(1000);
        WebElement formElement = driver.findElement(By.id("profile"));

        WebElement job = driver.findElement(By.id("job"));
        Select downList = new Select(job);
        downList.selectByIndex(2);
        downList.selectByValue("1");
        List<WebElement> list = downList.getAllSelectedOptions();
        for (WebElement option :list) {
            System.out.println(option.getText());
        }
        System.out.println(downList.getFirstSelectedOption().getText());

        //不咋用的
        downList.selectByVisibleText("学生");
    }

    /**
     * 鼠标操作
     */
    public void mouseOperate() {
        WebElement login = driver.findElement(By.className("menuContent"));
        List<WebElement> item = login.findElements(By.className("item"));

        Actions actions = new Actions(driver);
        //单击
        actions.click(login).perform();
        //双击
        actions.doubleClick(login).perform();
        this.sleep(2000);
        //鼠标移动到指定元素
        actions.moveToElement(item.get(0)).perform();
        windowsHandle =  driver.getWindowHandle();

        //查找指定的元素并点击
        driver.findElement(By.linkText("HTML/CSS")).click();
    }

    /**
     * 必须登录才能使用
     */
    public void iframe() {
        driver.get("http://www.imooc.com/wiki/create");
        WebElement iframeElement = driver.findElement(By.id("ueditor_0"));
        driver.switchTo().frame(iframeElement);
        driver.findElement(By.tagName("body")).sendKeys("this is test");
    }

    public void windowsHandle(){
        Set<String> handles = driver.getWindowHandles();
        for (String s : handles) {
            if (s.equals(windowsHandle)) {
                continue;
            }

            System.out.println(s);
            driver.switchTo().window(s);
        }
        driver.findElement(By.linkText("案例")).click();
    }


    private void sleep(int i) {
        try {
            Thread.sleep(i);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


    public void waitforElement() {
        //隐士等待
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        WebDriverWait wait = new WebDriverWait(driver,10);
        //找指定元素， 如果10s没有找到报错
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("test")));
    }

    public static void main(String[] args) {
        SeleniumTagOperateTest si = new SeleniumTagOperateTest();
        si.InitDriver();
        //si.inputBox();
        //si.radioBox();
        //si.checkBox();
//        si.button();
//        si.webForm();
//        si.upHeader();
//        si.downSlectBox();
        si.iframe();
    }

}