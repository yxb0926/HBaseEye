package com.hbaseeye.controller;

import com.hbaseeye.service.KpiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Controller
@RequestMapping("/api")
public class ApiController {

    @Autowired
    private KpiService kpiService;

    @ResponseBody
    @RequestMapping(value = "/kpi", method = RequestMethod.GET)
    public List kpi(HttpServletRequest request){
        String type       = request.getParameter("type");
        String tag        = request.getParameter("tag");
        String serverName = request.getParameter("serverName");
        String startTime  = request.getParameter("startTime");
        String  endTime   = request.getParameter("endTime");

        List kpiList = kpiService.getKpi(type, tag, serverName, startTime, endTime);
        return kpiList;
    }
}
