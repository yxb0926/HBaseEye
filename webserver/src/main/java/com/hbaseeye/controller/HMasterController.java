package com.hbaseeye.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Controller
@RequestMapping("/")
public class HMasterController {

    @RequestMapping("/hmaster")
    public ModelAndView hMaster(){
        ModelAndView modelAndView = new ModelAndView("hmaster");
        return modelAndView;
    }
}
