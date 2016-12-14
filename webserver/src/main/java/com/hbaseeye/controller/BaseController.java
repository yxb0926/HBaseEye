package com.hbaseeye.controller;

import com.hbaseeye.service.RequestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;

/**
 * Created by yuanxiaobin on 16/12/1.
 */
@Controller
@RequestMapping("/mng")
public class BaseController {

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
}
