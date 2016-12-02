package com.hbaseeye.controller;

import com.hbaseeye.service.RequestService;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;

/**
 * Created by yuanxiaobin on 16/12/1.
 */
@Controller
@RequestMapping("/mng")
public class BaseController {
    private Logger logger = Logger.getLogger(BaseController.class);

    @Autowired
    private RequestService requestService;

    @RequestMapping("/xxx")
    @ResponseBody
    public Object index(HttpServletRequest request){

        String hostname = request.getParameter("hostname");
        long   starttime = Long.parseLong(request.getParameter("starttime"));
        long   endtime   = Long.parseLong(request.getParameter("endtime"));

        return requestService.getQps(hostname, starttime, endtime);
    }

    @RequestMapping("/abc")
    public ModelAndView abc(HttpServletRequest request){
        System.out.println("abcxxxxxxxxxxxxxxxx");
        ModelAndView modelAndView = new ModelAndView("index");
        return modelAndView;
    }
}
