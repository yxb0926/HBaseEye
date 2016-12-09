package com.hbaseeye.controller;

import com.hbaseeye.model.ClusterInfo;
import com.hbaseeye.service.ClusterService;
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
public class ClusterController {

    @Autowired
    private ClusterService clusterService;

    @RequestMapping(value = "/cluster", method = RequestMethod.GET)
    public ModelAndView cluster(HttpServletRequest request){
        ModelAndView modelAndView = new ModelAndView("cluster");
        List<ClusterInfo> clusterInfo = clusterService.getClusterInfo();
        modelAndView.addObject("clusterinfo", clusterInfo);

        return modelAndView;
    }
}
