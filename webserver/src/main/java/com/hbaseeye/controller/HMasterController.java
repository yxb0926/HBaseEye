package com.hbaseeye.controller;

import com.hbaseeye.model.ClusterInfo;
import com.hbaseeye.service.ClusterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Controller
@RequestMapping("/")
public class HMasterController {

    @Autowired
    private ClusterService clusterService;

    @RequestMapping("/hmaster")
    public ModelAndView hMaster(){
        ModelAndView modelAndView = new ModelAndView("hmaster");

        List<ClusterInfo> clusterInfo = clusterService.getClusterInfo();
        modelAndView.addObject("hmasterinfo", clusterInfo);
        return modelAndView;
    }
}
