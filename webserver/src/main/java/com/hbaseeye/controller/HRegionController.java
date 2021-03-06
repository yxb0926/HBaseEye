package com.hbaseeye.controller;

import com.hbaseeye.model.ClusterInfo;
import com.hbaseeye.service.ClusterService;
import com.hbaseeye.service.HRegionServerService;
import com.hbaseeye.utils.DateTime;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Controller
@RequestMapping("/")
public class HRegionController {

    @Autowired
    private HRegionServerService hRegionServerService;

    @RequestMapping(value = "/hregion", method = RequestMethod.GET)
    public ModelAndView hRegion(HttpServletRequest request){
        ModelAndView modelAndView = new ModelAndView("hregion");
        List regionInfo = hRegionServerService.getRegionInfo();
        modelAndView.addObject("hregioninfo", regionInfo);

        DateTime dateTime = new DateTime();
        String startTime = dateTime.getTimeStr(6*60);  //6小时前时间
        String endTime = dateTime.getTimeStr(0);

        modelAndView.addObject("startTime", startTime);
        modelAndView.addObject("endTime",   endTime);


        return modelAndView;
    }

    @RequestMapping(value = "/hregionkpi", method = RequestMethod.GET)
    public ModelAndView hRegionKpi(HttpServletRequest request){
        String hostName = request.getParameter("hostName");
        ModelAndView modelAndView = new ModelAndView("hregionkpi");
        modelAndView.addObject("hostname", hostName);

        DateTime dateTime = new DateTime();
        String startTime = dateTime.getTimeStr(6*60);  //6小时前时间
        String endTime = dateTime.getTimeStr(0);

        modelAndView.addObject("startTime", startTime);
        modelAndView.addObject("endTime",   endTime);

        return modelAndView;
    }
}
